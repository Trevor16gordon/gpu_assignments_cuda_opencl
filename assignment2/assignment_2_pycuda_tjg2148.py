
class cudaCipher:
    def __init__(self):
        """
        Attributes for instance of deviceAdd module
        Includes kernel code and input variables.
        """
        # If you are using any helper function to make 
        # blocksize or gridsize calculations, you may define them
        # here as lambda functions. 
        # Quick lambda function to calculate grid dimensions
        
        # define block and grid dimensions
        #
        
        
        # kernel code wrapper
        #
        

        # Compile the kernel code when an instance
        # of this class is made.

    
    def devCipher(self, sentence):
        """
        Function to perform on-device parallel ROT-13 encrypt/decrypt
        by explicitly allocating device memory for host variables using
        gpuarray.
        Returns
            out                             :   encrypted/decrypted result
            time_ :   execution time in milliseconds
        """
        # Get kernel function

        # Device memory allocation for input and output array(s)
        
        # Record execution time and execute operation.
        
        # Wait for the event to complete

        # Fetch result from device to host

        # Convert output array back to string

        return decrypted, time_

    
    def pyCipher(self, sentence):
        """
        Function to perform parallel ROT-13 encrypt/decrypt using 
        vanilla python.

        Returns
            decrypted                       :   encrypted/decrypted result
            time_         :   execution time in milliseconds
        """

        return decrypted, time_


if __name__ == "__main__":
    # Main code

    # Open text file to be deciphered.
    # Preprocess the file to separate sentences
    
    # Split string into list populated with '.' as delimiter.

    # Empty lists to hold deciphered sentences, execution times


    # Loop over each sentence in the list
    for _ in _______:
        
    # post process the string(s) if required
        
    # Execution time
    print("CUDA output cracked in ", tc, " milliseconds per sentence.")
    print("Python output cracked in ", tp, " milliseconds per sentence.")

    # Error check
    try:
        print("Checkpoint: Do python and kernel decryption match? Checking...")
        assert # something
        
    except _________:
        print("Checkpoint failed: Python and CUDA kernel decryption do not match. Try Again!")
        # dump bad output to file for debugging
        

    # If ciphers agree, proceed to write decrypted text to file
    # and plot execution times
    
    if #conditions met:
        print("Checkpoint passed!")
        print("Writing decrypted text to file...")

        # Write cuda output to file
        
        # Dot plot the  per-sentence execution times