class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

    # or return '[.]'.join(address.split('.'))
    # or return re.sub('\.', '[.]', address)
    # or return ''.join('[.]' if c == '.' else c for c in address)

    # or without built-in fucntions
    # def defangIPaddr(self, address: str) -> str:
    #     res=""
    #     for i in address:
    #         if i==".":
    #             res+="[.]"
    #         else:
    #             res+=i
    #     return res

"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address."""