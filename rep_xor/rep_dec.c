#include <stdio.h>
#include <stdlib.h>
#include <string.h>


unsigned char * extract_key_char( unsigned char * string,
		size_t string_length, unsigned int keylength );

unsigned char * decrypt_xor(char * string, size_t string_length, char * key, unsigned int keylength );

int main(int argc, char * argv[])
{

	size_t buff_len = 10000;
	char * input = malloc(buff_len * sizeof(*input));

	fgets(input, buff_len, stdin);

	size_t input_len = strlen(input);

	size_t dec_size = strlen(input) / 2;

	unsigned char * decoded = malloc(dec_size * sizeof(*decoded));
	unsigned char * dec_ptr = decoded;

	size_t i;

	for ( i = 0; i < input_len; i += 2 )
	{
		sscanf(input + i, "%2hhx", dec_ptr++);
	}

	printf("%d\n", input_len);
	printf("%d\n", i);
	printf("%s\n", decoded);

	
	unsigned int keylength;

	sscanf(argv[1], "%u", &keylength);


	unsigned char * key = extract_key_char(decoded, dec_size, keylength);

	key[2] = '0' ^ 'u' ^ key[2];

	printf("%s\n", key);

	unsigned char * dec = decrypt_xor(decoded, dec_size, key, keylength);

	printf("%s\n", dec);

	return 0;
}


unsigned char * extract_key_char( unsigned char * string, size_t string_length, unsigned int keylength )
{
	unsigned int char_count[0xff];
	unsigned char * key = malloc((keylength + 1) * sizeof(*key));
	key[keylength] = 0; // Null terminate for printing

	size_t i;
	unsigned int offset;

	for ( offset = 0; offset < keylength; offset++ )
	{
	
		/* Reset char count */
		for ( i = 0; i < 0xff; i++ )
		{
			char_count[i] = 0;
		}

		/* count the characters */
		for ( i = offset; i < string_length; i += keylength )
		{
			char_count[string[i]] += 1;
		}
	

		/* Find the maximum occuring character */
		int max_i = 0;
		for ( i = 0; i < 0xff; i++ )
		{
			if ( char_count[i] > char_count[max_i] )
			{
				max_i = i;
			}
		}

		/* In english 'e' is the most common character */
		key[offset] = ' ' ^ max_i;
	}

	return key;
}

unsigned char * decrypt_xor(char * string, size_t string_length, char * key, unsigned int keylength )
{
	unsigned char * decrypted_string = malloc( ( string_length + 1 ) * sizeof(decrypted_string));
	decrypted_string[string_length] = 0;
	size_t i;

	for ( i = 0; i < string_length; i++ )
	{
		decrypted_string[i] = string[i] ^ key[i % keylength];
	}

	return decrypted_string;

}


