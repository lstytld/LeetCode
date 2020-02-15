class Solution:
    def compress(self, chars: List[str]) -> int:

        write = 0
        read = 0
        num = 1
        while read < len(chars):
            if read + 1 == len(chars) or chars[read + 1] != chars[write]:
                write += 1
                if num > 1:
                    for i in str(num):
                        chars[write] = i
                        write += 1
                if read + 1 < len(chars):
                    chars[write] = chars[read + 1]
                num = 0

            read += 1
            num += 1

        return write
