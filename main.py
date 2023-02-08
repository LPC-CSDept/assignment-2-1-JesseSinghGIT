def main():
    ##################################################
    # Comlete your code here
    ##################################################

    # Input
    numM = int(input('Enter the number of males: ')) # input() retuns string value. Need to change it to INT variable. 
    # num = int(numM)
    numF = int(input('Enter the number of females: '))
    
    # Calculation
    # total = numM + numF
    percM = numM / (numM + numF) * 100
    percF = numF / (numM + numF) * 100

    print('The total number of students: ', '\t   ',(numM + numF))
    print ( 'Number of males and females' , '\t   ', numM, numF)
    # print ( 'Percentage of males and females', percM, percF)
    print (f'Percentage of males and females :  {percM: .2f} % {percF: .2f}%')

    pass


if __name__ == '__main__':
    main()
