class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        con = sentence.split(' ')
        
        lst = []
        for i in range(len(con)):
            if con[i].count('$') == 1 and con[i][0] == '$' and con[i][1:].isdigit():
                
                f = int(con[i][1:]) - (int(con[i][1:]) * (discount/100))
                f = format(f , '.2f')
                con[i] = '$' + str(f)
   
        return ' '.join(con)
        
            
            
        