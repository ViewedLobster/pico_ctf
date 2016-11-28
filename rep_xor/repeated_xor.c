#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_KEY_L 100

double normed_hamming_all_wnd( unsigned char *, size_t, unsigned int );

unsigned int hamming_weight_char( unsigned char c );
unsigned int hamming_weight_int ( unsigned int i );

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
	double hamming[MAX_KEY_L];

	for ( keylength = 2; keylength <= 30; keylength++)
	{
		double h = normed_hamming_all_wnd( decoded, dec_size, keylength );
		printf("%u: %f\n",keylength, h);
	}

}

double normed_hamming_all_wnd( unsigned char* string, size_t string_length, unsigned int keylength_guess)
{
	unsigned int num_windows = string_length/keylength_guess;
	size_t i, j, k;
	unsigned long norm_factor = (num_windows * num_windows - num_windows) * keylength_guess;

	unsigned long tot_hamming_weight = 0;
	unsigned int tmp_hamming;

	size_t base_pos1, base_pos2;

	for ( i = 0; i < num_windows; i++ )
	{
		for ( j = 0; j < num_windows; j++ )
		{
			if (i != j)
			{
				base_pos1 = i * keylength_guess;
				base_pos2 = j * keylength_guess;
				for ( k = 0; k < keylength_guess; k++ )
				{

					tmp_hamming = hamming_weight_char(
							string[base_pos1 + k] ^
							string[base_pos2 + k]);

					tot_hamming_weight = tot_hamming_weight + tmp_hamming;

				}
			}
		}
	}
	
	return (double)tot_hamming_weight/(double)norm_factor;
}

/* Counts the number of set bits in a the char c */
unsigned int hamming_weight_char( unsigned char c )
{
	unsigned int tmp_int = (unsigned int) c;
	return hamming_weight_int (tmp_int);
}

/* Counts the number of set bits in the unsigned int i */
unsigned int hamming_weight_int ( unsigned int i )
{
	i = i - ((i >> 1) & 0x55555555 ); /* Each 2-bit block in i now contains
					   * the number of set bits in the
					   * corresponding two bits in input */

	i = (i & 0x33333333) + ((i >> 2) & 0x33333333);	/* Each 4-bit block contains 
							 * the sum of the 
							 * corresponding bits above */

	return (((i + (i >> 4)) & 0x0f0f0f0f) * 0x01010101) >> 24; 
	 		/* Finally the 4th 8-bit block (highest significant byte)
			 * contains the number of set bits in input */
}


unsigned char * extract_key_char( unsigned char * string, size_t string_length, unsigned int keylength )
{
	unsigned int char_count[0xff];
	unsigned char * key = malloc(keylength * sizeof(*key));
	size_t i;
	unsigned int offset;

	for ( offset = 0; offset < keylength; offset++ )
	{
	
		for ( i = 0; i < 0xff; i++ )
		{
			char_count[i] = 0;
		}

		for ( i = offset; i < string_length; i += keylength )
		{
			char_count[string[i]] += 1;
		}
	
		int max_i = 0;

		for ( i = 0; i < 0xff; i++ )
		{
			if ( char_count[i] > char_count[max_i] )
			{
				max_i = i;
			}
		}

		
		key[offset] = 'e' ^ max_i;
	}

	return key;

}


