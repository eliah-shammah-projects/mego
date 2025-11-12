

MIN_CELLS = 10
MAX_CELLS = 30
NUM_COINS = 4

def print_welcome_message() -> None:
     print ("Hello! Let's start the game!")

def get_cellnum() -> int:
     cellnum = int(input("Enther the number of cells"))
     while cellnum < MIN_CELLS or cellnum > MAX_CELLS:
          print ("invalid number")
          cellnum = int(input("Enther the number of cells"))
     return cellnum

def place_coins(cellnum: int) -> list[int]:
     
    lis = []

    for i in range (4):
        place = int(input("enter the num of place"))
        while (place < 0 or place > cellnum) or place in lis:
                print ("invalid number")
                place = int(input("enter the num of place"))
        lis.append(place) 
    lis.sort()
    return lis

def draw_board(coins: list[int], cellnum: int) -> None:
    print("indexs:", end=" ")
    for i in range(cellnum):
        print(f"{i},", end=" ")
    print("")  

    print("valors:", end=" ")
    index = 0
    for y in range(cellnum):
        if y != coins[index]:
            print("_,", end=" ")
        else:
            print(f"X,", end=" ")
            index += 1
    print("")  

def gameover(coins: list[int]) -> bool:
    
    flag = True
    for i in range (3):
          
        if coins[i] + 1 != coins [i + 1]:
            flag = False
            break 
    
    if flag and coins[0] == 0:
         return True
    return False

def make_move(coins: list[int], player: int) -> None:

    coin = int(input("enter the coin number"))
    stap = int(input("enter the number of staps that you want to do"))
    index = coins[coin-1]
    new_index = index - stap
    while new_index < 0:
        coin = int(input("enter the coin number"))
        stap = int(input("enter the number of staps that you want to do"))
        index = coins[coin-1]
        new_index = index - stap
    
    while new_index <= coins[coin - 2] and coin != 1:
        coin = int(input("enter the coin number"))
        stap = int(input("enter the number of staps that you want to do"))
        index = coins[coin-1]
        new_index = index - stap
    
    coins[coin - 1] = new_index
              
         
def print_game_summary(winner: int) -> None:
     
     print ("Game end!", winner, "win!!!")


def  draw_line(length: int) -> None:
    print("-" * length)



def main():
    player_num = 1
    coins = []
    print_welcome_message ()
    cellnum = get_cellnum()
    coins = place_coins(cellnum)
    draw_board (coins, cellnum)
    draw_line(cellnum * 3)

    while not gameover (coins):
         make_move (coins, player_num)
         draw_board (coins, cellnum)
         draw_line(cellnum * 3)
         player_num = 3 - player_num

    print_game_summary(3 - player_num)
            
    
    
               
        
             
             
        

     

          
     


