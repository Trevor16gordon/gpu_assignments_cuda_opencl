

class clCipher:
    def __init__(self):
        """
        Attributes for instance of clModule
        Includes OpenCL context, command queue, kernel code
        and input variables.
        """
        
        # Get platform and device property
        NAME = 'NVIDIA CUDA'
        platforms = cl.get_platforms()
        devs = None
        for platform in platforms:
        	if platform.name == NAME:
        		devs = platform.get_devices()       
        
        # Set up a command queue:
        self.ctx = cl.Context(devs)
        self.queue = cl.CommandQueue(self.ctx, properties=cl.command_queue_properties.PROFILING_ENABLE)
        
        # kernel
        
        # Build kernel code
        

    def devCipher(self, sentence):
        """
        Function to perform on-device parallel ROT-13 encrypt/decrypt
        by explicitly allocating device memory for host variables.
        Returns
            decrypted :   decrypted/encrypted result
            time_     :   execution time in milliseconds
        """

        # Text pre-processing/list comprehension (if required)
        # Depends on how you approach the problem
        
        # device memory allocation
        
        # Call the kernel function and time event execution
        
        # OpenCL event profiling returns times in nanoseconds. 
        # Hence, 1e-6 will provide the time in milliseconds, 
        # making your plots easier to read.

        # Copy result to host memory
        
        return decrypted, time_

    
    def pyCipher(self, sentence):
        """
        Function to perform parallel ROT-13 encrypt/decrypt using 
        vanilla python. (String manipulation and list comprehension
        will prove useful.)

        Returns
            decrypted                  :   decrypted/encrypted result
            time_    :   execution time in milliseconds
        """
        
        return decrypted, time_


if __name__ == "__main__":
    # Main code

    # Open text file to be deciphered.
    # Preprocess the file to separate sentences


    # Loop over each sentence in the list
    for _ in _______:
        
    # Stitch decrypted sentences together
    
    print("OpenCL output cracked in ", tc, " milliseconds per sentence.")
    print("Python output cracked in ", tp, " milliseconds per sentence.")

    # Error check
    try:
        print("Checkpoint: Do python and kernel decryption match? Checking...")
        # compare outputs
    except ______:
        print("Checkpoint failed: Python and OpenCL kernel decryption do not match. Try Again!")
        # dump bad output to file for debugging
        

    # If ciphers agree, proceed to write decrypted text to file
    # and plot execution times

    if #conditions met: 

        # Write cuda output to file
        
        # Scatter plot the  per-sentence execution times    