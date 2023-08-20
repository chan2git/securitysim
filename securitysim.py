import random
import json

"""
A python module that simulates various data and scripts that may be useful for security professionals.

How to import:
    Save this module in the same working directory as your py file, and import the module:
        >>> import securitysim

How to call functions:
    Format: securitysim.<function_name(<parameter>)>

    Example: securitysim.generate_ip_list(25)
"""



def generate_ip():
    """
    Function that returns a realistic public IP address

    Args:
        none

    Returns:
        string: a realistic public IP address

    Example:
        >>> ip = securitysim.generate_ip()
            print(ip)

        Output
            119.9.87.129
    """

    while True:
        octet1 = random.randint(1, 255)
        octet2 = random.randint(0, 255)
        octet3 = random.randint(0, 255)
        octet4 = random.randint(1, 254)  # Exclude 0 and 255 for the last octet

        ip_address = f"{octet1}.{octet2}.{octet3}.{octet4}"
        
        '''
        Used ChatGPT for the if statement logic to only return a IP address that excludes:
        - Private address ranges (RFC 1918)
        - Loopback addresses
        - Link-local addresses
        - Reserved multicast addresses
        - Reserved broadcast addresses
        - Unique local address (ULA) range
        - Multicast addresses
        '''

        if (octet1 != 10) and \
            (octet1 != 172 or not (16 <= octet2 <= 31)) and \
            (octet1 != 192 or octet2 != 168) and \
            not (octet1 == 169 and octet2 == 254) and \
            (octet1 != 224) and \
            (octet1 != 0) and \
            (octet1 != 255) and \
            not (octet1 == 100 and 64 <= octet2 <= 127) and \
            not (224 <= octet1 <= 239):
                return ip_address
 





def generate_ip_list (num_addresses):
    """
    Function that generates a list of realistic public IP addresses

    Args:
        num_addresses (int): The quantity of IP addresses to generate

    Returns:
        list: a list of generated IP addresses

    Example:
        >>> ip_list = securitysim.generate_ip_list(3)
            print(ip_list)

        Output:
            ['118.65.168.116', '97.134.249.126', '187.130.144.31'] 
    """

    ip_address_list = []

    for i in range(num_addresses):
        ip_address = generate_ip()
        ip_address_list.append(ip_address)
    
    return ip_address_list






def generate_ip_country_list (num_addresses):
    """
    Function that generates a list of countries randomly chosen from a pre-defined list, and associates it to randomly generated IP addresses

    Args:
        num_addresses (int): The quantity of IP addresses to generate

    Returns:
        list: a list of generated IP addresses that is associated to a country

    Example:
        >>> ip_country = securitysim.generate_ip_country_list(3)
            print(ip_country)

        Output:
            [{'src IP address: 93.98.32.230, src_country: China'}, {'src IP address: 77.203.6.142, src_country: China'}, {'src IP address: 141.69.29.100, src_country: Russia'}]
    """

    ip_country_list = []
    country_list = ["United States", "Canada", "China", "North Korea", "Russia", "Singapore", "Mexico", "United Kingdom", "Japan"]

    for i in range(num_addresses):
        ip_address = generate_ip()
        country = random.choice(country_list)

        pair = {f"src IP address: {ip_address}, src_country: {country}"}
        
        ip_country_list.append(pair)

    return ip_country_list





def defang (string):
    """
    Function that accepts a string and defangs it

    Args:
        string (string): A string representing a URL or IP address to be defanged

    Returns:
        defanged_string (string): a defanged version of the provided string

    Example:
        >>> print(securitysim.defang("https://www.example.com"))

        Output:
            hxxps://www[.]example[.]com
    """
    
    # Use case for URLs
    if "://" in string or "www" in string:
        defanged_string = string.replace('.', '[.]')
        defanged_string = defanged_string.replace('https', 'hxxps')
        defanged_string = defanged_string.replace('http', 'hxxp')
    
    # Use case for URLs without 'https', 'http', or 'www', and use case for IP addresses
    elif "." in string:
        defanged_string = string.replace('.', '[.]')
    
    # Error message if invalid string
    else:
        return "Error. Please double check if string is a correctly formatted URL or IP address"

    return defanged_string





def defang_list (list):
    """
    Function that accepts a list of strings and defangs it

    Args:
        list (list): A list containing URLs and or IP addresses to be defanged

    Returns:
        defanged_list (list): a defanged veesion of the provided list

    Example:
        >>> list = ['http://badwebsite.com', 'www.malicioussite.com', 'https://www.example.com']
            df_list = securitysim.defang_list(list)
            print(df_list)

        Output:
            ['hxxp://badwebsite[.]com', 'www[.]malicioussite[.]com', 'hxxps://www[.]example[.]com']
    """

    defanged_list = []

    for string in list:
        defanged_string = defang(string)
        defanged_list.append(defanged_string)

    return defanged_list













#############################
# Version:    1.00          #
# Date:       08/20/2023    #
# Coder:      CH @chan2git  #
#############################