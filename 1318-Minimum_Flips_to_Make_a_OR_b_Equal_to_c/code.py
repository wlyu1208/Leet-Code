class Solution:
    def to_binary(self, n: int):
            return format(n, 'b')
    
    def fill_zero(self, binary, _max):
        return ('0' * (_max - len(binary)) + binary)

    def minFlips(self, a: int, b: int, c: int) -> int:
        nums = [a, b, c]
        
        bins = list()
        max_len = 0
        
        for x in nums:
            binary = self.to_binary(x)
            bins.append(binary)
            if len(binary) > max_len:
                max_len = len(binary)
        
        for i in range(len(bins)):
            binary = bins[i]
            if len(binary) < max_len:
                bins[i] = self.fill_zero(binary, max_len)

        result = 0
        a = bins[0]
        b = bins[1]
        c = bins[2]

        for i in range(max_len):
            _a = int(a[i])
            _b = int(b[i])
            _c = int(c[i])
            
            if _c == 1 and _a == 0 and _b == 0:
                result += 1
            elif _c == 0:
                if _a == 1 and _b == 0:
                    result += 1
                elif _a == 1 and _b == 1:
                    result += 2
                elif _a == 0 and _b == 1:
                    result += 1
        return result

