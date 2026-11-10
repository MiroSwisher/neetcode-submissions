class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += "(" + str(len(s)) + ")" + s
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        while len(s) > 0:
            left_paren_idx = 0
            right_paren_idx = s.find(")")

            length = int(s[left_paren_idx + 1:right_paren_idx])
            s = s[2 + len(str(length)):]

            s_recon = s[0:length]

            result.append(s_recon)

            s = s[length:]
        return result