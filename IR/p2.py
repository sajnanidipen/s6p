def find_main_rank(lis):
     copylis=lis.copy()
     ranks=[0,0,0,0]
     copylis.sort()
     
     for i in range(0,len(lis)):
          ranks[i]=lis.index(copylis[i])
     ranks.reverse()
     print("ranks are ",ranks)

def page_Rank(pageranks,outlinks,n,matrix,d=0.85):
     old=pageranks.copy()
     sum1=0
     for i in range(0,4):
          sum1=0
          for j in range(0,4):
               if matrix[i][j]==1:
                    sum1=sum1+(old[j]/outlinks[j])

          pageranks[i]=(1-d)/4+d*sum1
          
     if n>0:
          page_Rank(pageranks,outlinks,n-1,matrix)
     else:
          print(pageranks)
          find_main_rank(pageranks)
          
pageranks=[1/4,1/4,1/4,1/4]
outlinks=[2,1,3,1]
matrix=[[0,0,1,0],[1,0,1,0],[1,0,0,1],[0,1,1,0]]
iterations=3
page_Rank(pageranks,outlinks,iterations,matrix)



                    
     
          
          
          
          
          
