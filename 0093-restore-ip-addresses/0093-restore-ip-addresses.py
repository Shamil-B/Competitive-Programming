class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        validAddresses = []
        unique = set()
        def backtrack(addresses,string):

            if not string and len(addresses) == 4:
                ipAdd = ".".join(addresses)
                if ipAdd not in unique:
                    validAddresses.append(ipAdd)
                    unique.add(ipAdd)

                return

            if len(addresses) >= 4:
                return 

            candidates = [string[:i] for i in range(1,4)]

            for candidate in candidates:
                if candidate and int(candidate) >= 0 and int(candidate) < 256 and (len(candidate) == len(str(int(candidate)))):
                    addresses.append(candidate)
                    backtrack(addresses[:],string[len(candidate):])
                    addresses.pop()

        backtrack([],s)
        return validAddresses