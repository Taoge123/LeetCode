import collections
class Solution:
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """

        width, height = len(picture), len(picture[0])
        rows, cols = [0] * width, [0] * height

        #build array counnter storing counts of 'B' in each row and col
        for x in range(width):
            for y in range(height):
                if picture[x][y] == 'B':
                    rows[x] += 1
                    cols[y] += 1

        #HashMap that stores how distict rows as key and count as value
        sdict = collections.defaultdict(int)
        for idx, row in enumerate(picture):
            sdict[''.join(row)] += 1
            # print(sdict)

        ans = 0

        #Loop through each row
        for x in range(width):
            row = ''.join(picture[x])
            print(row)

            #Only if there are N rows are identica, it will makes rule 2 valid
            if sdict[row] != N:
                continue
            for y in range(height):

                if picture[x][y] == 'B' and rows[x] == N and cols[y] == N:
                    ans += 1


        print(ans)
        return ans


s = Solution()
s.findBlackPixel([["W","B","W","B","B","W"],
                  ["W","B","W","B","B","W"],
                  ["W","B","W","B","B","W"],
                  ["W","W","B","W","B","W"]], 3)

