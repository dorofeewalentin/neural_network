def create_combinations(self, big_list):
        max_procent = -1000
        
        #final_list = np.zeros((11, self.lt))
        
        final_list = [[] for x in range(11)]
        for fl in range(len(final_list)):
            final_list[fl]  = [0 for x in range(self.lt)]
        
        n = self.nt
        i = 0
        check_list = []
        count = 0
        index = []
        count2 = 0
        for i in range(1, n):
            count += n**i
        count *= 100
        l = count
        receipt = [[] for x in range(l)]
        print("l = ", l)
        #other_list = np.empty((l, self.lt))
        other_list = [[] for x in range(l)]
        #for ol in range(len(other_list)):
            #other_list[ol] = [0 for x in range(self.lt)]
        index_list = [0]
        count = 0
        count2 = 0
        for t in range(n):
            count3 = count2
            count2 = 0
            count5 = count
            count4 = count - count3
            helpcount4 = count4
            helpcount5 = count5
            for e in range(n):
                if t == 0:
                    other_list[count] = big_list[e]
                    receipt[count].append(e + 1)
                    count += 1
                    count2 += 1
                else:
                    while count4 < count5:
                        for i in range(self.lt):
                            #if count < l and count4 < l:
                            '''
                            print("count4 = ", count4)
                            print("len final_list = ", len(final_list))
                            print("len final_list[0] = ", len(final_list[0]))
                            print("len other_list = ", len(other_list))
                            print("len big_list = ", len(big_list))
                            print("e = ", e)
                            print("i = ", i)
                            '''
                            
                            #1
                            if count4 == count:
                                if big_list[e][i] == other_list[count4][i]:
                                    final_list[0][i] = big_list[e][i]
                                else:
                                    final_list[0][i] = 0 
                            #2
                            if big_list[e][i] == 1:
                                final_list[1][i] = 1
                            else:
                                final_list[1][i] = other_list[count4][i]
                            #3
                            if big_list[e][i] == 2:
                                final_list[2][i] = 2
                            else:
                                final_list[2][i] = other_list[count4][i]
                            #4
                            if other_list[count4][i] == 1:
                                final_list[3][i] = 1
                            else:
                                final_list[3][i] = big_list[e][i]
                            #5
                            if other_list[count4][i] == 2:
                                final_list[4][i] = 2
                            else:
                                final_list[4][i] = big_list[e][i]
                            #6
                            if big_list[e][i] == 1 and other_list[count4][i] == 0:
                                final_list[5][i] = 1
                            else:
                                final_list[5][i] = other_list[count4][i]
                            #7
                            if big_list[e][i] == 2 and other_list[count4][i] == 0:
                                final_list[6][i] = 2
                            else:
                                final_list[6][i] = other_list[count4][i]
                            #8
                            if other_list[count4][i] == 1 and big_list[e][i] == 0:
                                final_list[7][i] = 1
                            else:
                                final_list[7][i] = big_list[e][i]
                            #9
                            
                            if other_list[count4][i] == 2 and big_list[e][i] == 0:
                                final_list[8][i] = 2
                            else:
                                final_list[8][i] = big_list[e][i]
                            #10
                            if big_list[e][i]!= 0:
                                final_list[9][i] = big_list[e][i]
                            if other_list[count4][i] != 0 and big_list[e][i] == 0:
                                final_list[9][i] = other_list[count4][i] 
                            #11
                            if other_list[count4][i]!= 0:
                                final_list[10][i] = other_list[count4][i]
                            if big_list[e][i] != 0 and other_list[count4][i] == 0:
                                final_list[10][i] = big_list[e][i] 
                        for a in range(len(final_list)):
                            check = True
                            
                            check2 = True
                            for ch in range(count):
                                check2 = True
                                for ch2 in range(self.lt):
                                    if final_list[a][ch2] != other_list[ch][ch2]:
                                        check2 = False
                                if check2 == True:
                                    check = False
                                    
                            if check == True:
                                receipt[count] = list(receipt[count4])
                                receipt[count].append(e + 1)
                                receipt[count].append('var' + str(a + 1))
                                print(receipt[count])
                                other_list[count] = final_list[a]
                                procent = self.offline_for_rf(other_list[count])
                                print(procent)
                                if procent > max_procent:
                                    print("max procent:", procent)
                                    max_procent = procent
                                    best_list = list(other_list[count])
                                    best_receipt = list(receipt[count])
                                    print("best receipt: ", best_receipt)
                                    print("best list: ", best_list)
                                count += 1
                                count2 += 1      
                        count4 += 1
                        final_list[9] = [0 for x in range(self.lt)]
                        final_list[10] = [0 for x in range(self.lt)]
                    count4 = helpcount4
                    count5 = helpcount5
                    #print(other_list[:count])
                    #other_list[:count + 10] = [el for el, _ in groupby(other_list[:count + 10])]
                    #other_list[:count] = f(other_list[:count])
        return_list = [best_list, best_receipt]
        return return_list
        pass
