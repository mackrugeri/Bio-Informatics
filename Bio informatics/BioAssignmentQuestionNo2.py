def zeros(shape):
    retval = []
    for x in range(shape[0]):
        retval.append([])
        for y in range(shape[1]):
            retval[-1].append(0)
    return retval
def match_score(alpha, beta,match_award,mismatch_penalty,gap_penalty):
    if alpha == beta:
        return match_award
    elif alpha == '-' or beta == '-':
        return gap_penalty
    else:
        return mismatch_penalty
def optimal_Aligment(seq1, seq2,match_award,mismatch_penalty,gap_penalty):
    m, n = len(seq1), len(seq2) 
    score = zeros((m+1, n+1))      
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score[i - 1][j - 1] + match_score(seq1[i-1], seq2[j-1],match_award,mismatch_penalty,gap_penalty)
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            score[i][j] = max(match, delete, insert)
    align1, align2 = [], []
    i,j = m,n
    while i > 0 and j > 0:
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_up = score[i][j-1]
        score_left = score[i-1][j]
        if score_current == score_diagonal + match_score(seq1[i-1], seq2[j-1],match_award,mismatch_penalty,gap_penalty):
            align1.append(seq1[i-1])
            align2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif score_current == score_left + gap_penalty:
            align1.append(seq1[i-1])
            align2.append('-')
            i -= 1
        elif score_current == score_up + gap_penalty:
            align1.append('-')
            align2.append(seq2[j-1])
            j -= 1
    while i > 0:
        align1.append(seq1[i-1])
        align2.append('-')
        i -= 1
    while j > 0:
        align1.append('-')
        align2.append(seq2[j-1])
        j -= 1 
        
    print("The optimal Alignment is: ")
    i= len(align1)-1
    while(i>=1):
        print(align1[i],end="")
        i = i-1
    i= len(align2)-1
    print("\n")
    while(i>=1):
        print(align2[i],end="")
        i = i-1
   
        
def match_mismatch(Match,Mismatch,S1,S2):
    if S1 == S2:
        return Match
    else:
        return Mismatch
def questionNo2(filename):
    Seq = []
    with open(filename,'r') as f:
        for line in f:
            Seq.append(line)
            
        match = int(input("Enter the score for match: "))
        Mis = int(input("Enter the score for Mismatch: "))
        indel = int(input("Enter the score for indel: "))

        length1 = len(Seq[0])-1
        length2 = len(Seq[1])
        Matrix = [[0 for x in range(length1+1)] for y in range(length2+1)]
        
        Matrix[0][0] = 0
        for i in range(1,length2+1):
            Matrix[0][i] = i*indel
        for i in range(1,length1+1):
            Matrix[i][0] = i*indel
        for i in range(1,length1+1):
            for j in range(1,length2+1):
                Second = Seq[0]
                first = Seq[1]
                result = Matrix[i-1][j-1]+ match_mismatch(match,Mis,first[j-1],Second[i-1])
                result1 = Matrix[i][j-1]+indel
                result2 = Matrix[i-1][j]+indel
                Matrix[i][j]=max(result,result1,result2)
        print("The Final Score is ",Matrix[length1][length2])
        optimal_Aligment(Seq[0],Seq[1],match,Mis,indel)

questionNo2("Bio_File2.txt")