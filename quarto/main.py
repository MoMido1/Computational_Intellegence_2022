# Free for personal or classroom use; see 'LICENSE.md' for details.
# https://github.com/squillero/computational-intelligence

import logging
import argparse
import random
import quarto
import numpy as np
import sys

new_limit = 50000  # Example: Setting a new recursion limit of 5000
sys.setrecursionlimit(new_limit)

class RandomPlayer(quarto.Player):
    """Random player"""

    def __init__(self, quarto: quarto.Quarto) -> None:
        super().__init__(quarto)

    def choose_piece(self) -> int:
        return random.randint(0, 15)

    def place_piece(self) -> tuple[int, int]:
        return random.randint(0, 3), random.randint(0, 3)
    


# # self._Player__quarto.print()
# self.get_game().select(4)
# self.get_game().place(1,2)
# # print(self._Player__quarto.get_board_status())
# print(self.get_game().get_board_status())
# o =self.get_game().check_winner()
# if o:
#     self.get_game()._board[2,1]= -1
# # self.get_game().place(1,2)
# print(self.get_game().get_board_status())
# # self._Player__quarto.print()



class ExpertPlayer(quarto.Player):
    # here my algorithm extends the Player class and takes as an input the quarto object of Quarto class
    """Random player"""

    def __init__(self, quarto: quarto.Quarto) -> None:
        super().__init__(quarto)

    def is_a_win (self,l):
        high =0
        colored =0
        solid =0
        square =0
        for p_n in l:
            if p_n == -1:
                return False
            piece =self.get_game().get_piece_charachteristics(p_n)
            high += 1 if piece.HIGH else 0
            colored += 1 if piece.COLOURED else 0
            solid += 1 if piece.SOLID else 0
            square += 1 if piece.SQUARE else 0
        if high ==4 or colored ==4 or solid ==4 or square ==4:
            return True
        else:
            return False

    def get_score(self,l) -> int:
        high =0
        colored =0
        solid =0
        square =0
        score =0
        
        for p_n in l:
            # print(p_n)
            if p_n != -1:    
                piece =self.get_game().get_piece_charachteristics(p_n)
                high += 1 if piece.HIGH else 0
                colored += 1 if piece.COLOURED else 0
                solid += 1 if piece.SOLID else 0
                square += 1 if piece.SQUARE else 0
        
        score +=1 if high ==3 else 0
        score +=1 if colored ==3 else 0
        score +=1 if solid ==3 else 0
        score +=1 if square ==3 else 0
        
        return score  

    def piece_score (self,p) -> int:
        game = self.get_game()
        s =0
        if p in game._board:
            # this piece is not available
            return -1
        # if the piece will make a win i return -2
        # free_places = np.count_nonzero(game._board == -1)
        for i,row in enumerate(game._board):
            if -1 in row:
                for j,e in enumerate(row):
                    # print(game._board[:,j])
                    if e == -1 :
                        # print(i)
                        # print(j)
                        game._board[i,j] = p
                        reversed_arr = np.fliplr(game._board)
                        # print(row)
                        if self.is_a_win(row) or self.is_a_win(game._board[:,j]) or self.is_a_win(game._board.diagonal()) or self.is_a_win(reversed_arr.diagonal()):
                            game._board[i,j] = -1
                            return -2
                        else:
                            s += self.get_score(row) +self.get_score(game._board[:,j]) +self.get_score(game._board.diagonal()) + self.get_score(reversed_arr.diagonal())
                        game._board[i,j] = -1
        return s

        # print(self.is_a_win([1,5,9,15]))
        # return 0

    def choose_piece(self) -> int:
        # i will choose the piece that max the reward without making the win
        # loop for all pieces
        # each piece will have a score that is defined based on the number of 
        # 3's that this piece could form if it was placed in any place
        # and i choose the piece with the max 3's
        game = self.get_game()
        available_pieces = list()
        # print('choosing a piece')
        # available pieces
        
        for j in range(16):
            if j not in game._board:
                score= self.piece_score(j)
                available_pieces.append((j,score)) 
        
        # game._board[0,:]= [0,2,-1,-1]
        # game._board[1,:]= [-1,-1,7,8]
        # game._board[2,:]= [-1,10,-1,12]
        # game._board[3,:]= [13,-1,-1,15]
        

        
        # score =game._board[:,j]
        # if score == -1:
        #     #unavailable piece
        #     return 0

        # print('my selection is '+ str(sorted(available_pieces,key= lambda x:x[1],reverse=True)[0][0]))
        return sorted(available_pieces,key= lambda x:x[1],reverse=True)[0][0]

    def place_score(self,place,piece)-> int:
        i,j = place
        game = self.get_game()
        game._board[i,j] = piece
        s=0

        for row in game._board:
            reversed_arr = np.fliplr(game._board)
            if self.is_a_win(row)  or self.is_a_win(game._board.diagonal()) or self.is_a_win(reversed_arr.diagonal()):
                # game.print()
                return -2
            else:
                s += self.get_score(row) +self.get_score(game._board.diagonal()) + self.get_score(reversed_arr.diagonal())
                        
        for j in range(4):
            if self.is_a_win(game._board[:,j]):
                
                # print('dd')
                return -2
            else:
                s+= self.get_score(game._board[:,j])
        # no winning place

        return s
        

    
    def place_piece(self) -> tuple[int, int]:
        # check for the places that guarantees the win if not
        # place the piece in the place that after that will guarantee 
        # a low value
        # print('me putting a piece')
        game = self.get_game()
        piece = game.get_selected_piece()
        if piece == -1:
            return random.randint(0, 3), random.randint(0, 3)
        available_places = list()

        # available places
        # game.print()
        for i in range(4):
            for j in range(4):
                if game._board[i,j] == -1 :
                    # print(i,j)
                    p = i,j
                    score= self.place_score(p,piece)
                    game._board[i,j] = -1
                    # print('place Scroe is '+ str(score))
                    if(score == -2):
                        # print('eh')
                        return int(p[1]),int(p[0])
                    available_places.append((p,score)) 

        # print('my place that i decided is '+str(tuple(sorted(available_places,key=lambda x:x[1])[0][0])))
        place = sorted(available_places,key=lambda x:x[1])[0][0]
        return int(place[1]) , int(place[0])
    
    def get_game(self):
        
        return super().get_game()
    
class MinMaxPlayer(quarto.Player):
    """Min Max approach player"""

    def __init__(self, quarto: quarto.Quarto) -> None:
        super().__init__(quarto)

    def is_a_win (self,l):
        high =0
        colored =0
        solid =0
        square =0
        for p_n in l:
            if p_n == -1:
                return False
            piece =self.get_game().get_piece_charachteristics(p_n)
            high += 1 if piece.HIGH else 0
            colored += 1 if piece.COLOURED else 0
            solid += 1 if piece.SOLID else 0
            square += 1 if piece.SQUARE else 0
        if high ==4 or colored ==4 or solid ==4 or square ==4:
            return True
        else:
            return False

    def get_score(self,l) -> int:
        high =0
        colored =0
        solid =0
        square =0
        score =0
        
        for p_n in l:
            if p_n != -1:    
                piece =self.get_game().get_piece_charachteristics(p_n)
                high += 1 if piece.HIGH else 0
                colored += 1 if piece.COLOURED else 0
                solid += 1 if piece.SOLID else 0
                square += 1 if piece.SQUARE else 0
        
        score +=1 if high ==3 else 0
        score +=1 if colored ==3 else 0
        score +=1 if solid ==3 else 0
        score +=1 if square ==3 else 0
        
        return score  
    
    def current_game_score(self)->int:
        game = self.get_game()
        s=0
        for row in game._board:
            if -1 not in row :
                if self.is_a_win(row):
                    return -2
            s += self.get_score(row)
        for i in range(4):
            if -1 not in game._board[:,i] :
                if self.is_a_win(game._board[:,i]):
                    return -2
            s+= self.get_score(game._board[:,i])
        if self.is_a_win(game._board.diagonal()):
            return -2
        else:
            s += self.get_score(game._board.diagonal())

        reversed_arr = np.fliplr(game._board)
        if self.is_a_win(reversed_arr.diagonal()):
            return -2
        else:
            s += self.get_score(reversed_arr.diagonal())
        return s         

    def piece_score (self,p) -> int:
        game = self.get_game()
        s =0
        if p in game._board:
            return -1
        # if the piece will make a win i return -2
        # free_places = np.count_nonzero(game._board == -1)
        for i,row in enumerate(game._board):
            if -1 in row:
                for j,e in enumerate(row):
                    if e == -1 :
                        game._board[i,j] = p
                        reversed_arr = np.fliplr(game._board)
                        if self.is_a_win(row) or self.is_a_win(game._board[:,j]) or self.is_a_win(game._board.diagonal()) or self.is_a_win(reversed_arr.diagonal()):
                            game._board[i,j] = -1
                            return -2
                        else:
                            s += self.get_score(row) + self.get_score(game._board[:,j]) +self.get_score(game._board.diagonal()) + self.get_score(reversed_arr.diagonal())
                        game._board[i,j] = -1
        return s


    def MinMax_piece(self):
        game = self.get_game()
        available_pieces = list()
        for j in range(16):
            if j not in game._board:
                available_pieces.append(j)
        old_piece = game.get_selected_piece()
        eval= self.current_game_score()
        if eval == -2 or len(available_pieces)==0:
            game.select(old_piece)
            return None,eval
        
        evaluations = list()
        for piece in available_pieces:
            o_p = game.get_selected_piece()
            game.select(piece)
            x,y =self.place_extreme_piece()
            game._board[y,x] = piece
            _,val = self.MinMax_piece()
            
            if np.count_nonzero(game._board == -1) == 1:
                evaluations.append((piece,-2))
            else:
                val= self.current_game_score()
                evaluations.append((piece,val))
            game._board[y,x]= -1
            game.select(o_p)
        game.select(old_piece)
        selected_piece = sorted(evaluations,key= lambda x:x[1], reverse=True)[0]
        return selected_piece
   
    def choose_extreme_piece(self,t=True)-> int:
        # t=True he will select the piece with highest score 8,7,-1  then 8
        # here i want to choose a piece that will gaurantee for him the loose
        game = self.get_game()
        available_pieces = list()
        for j in range(16):
            if j not in game._board:
                score= self.piece_score(j)
                available_pieces.append((j,score)) 
        available_pieces =sorted(available_pieces,key= lambda x:x[1],reverse=t)
        return available_pieces[0][0]


    def choose_piece(self) -> int:
        # my goal here is to choose the piece that gives 
        # the min reward
        num = self.MinMax_piece()
        return num[0]
    
    def place_score(self,place,piece)-> int:
        i,j = place
        game = self.get_game()
        game._board[i,j] = piece
        s=0

        for row in game._board:
            reversed_arr = np.fliplr(game._board)
            if self.is_a_win(row)  or self.is_a_win(game._board.diagonal()) or self.is_a_win(reversed_arr.diagonal()):
                # game.print()
                return -2
            else:
                s += self.get_score(row) +self.get_score(game._board.diagonal()) + self.get_score(reversed_arr.diagonal())      
        for j in range(4):
            if self.is_a_win(game._board[:,j]):
                return -2
            else:
                s+= self.get_score(game._board[:,j])
        # no winning place

        return s
        
    def place_extreme_piece(self) -> tuple[int, int]:
        # he will place it in the best place
        game = self.get_game()
        piece = game.get_selected_piece()
        if piece == -1:
            return random.randint(0, 3), random.randint(0, 3)
        available_places = list()
        for i in range(4):
            for j in range(4):
                if game._board[i,j] == -1 :
                    p = i,j
                    score= self.place_score(p,piece)
                    game._board[i,j] = -1
                    if score == -2:
                        return int(p[1]),int(p[0])
                    if score != -1:
                        available_places.append((p,score)) 
        place = sorted(available_places,key=lambda x:x[1],reverse=False)[0][0]
        # print(place)
        return int(place[0]) , int(place[1])
    
    def MinMax_place(self):
        game = self.get_game()
        piece = game.get_selected_piece()
        if piece == -1:
            return random.randint(0, 3), random.randint(0, 3)
        available_places = list()
        for i in range(4):
            for j in range(4):
                if game._board[i,j] == -1 :
                    p = i,j
                    available_places.append(p) 
        val = self.current_game_score()
        
        if val == -2 or len(available_places) == 1 :
            return available_places[0], val
        
        evaluations= list()
        for place in available_places:
            game._board[place[0],place[1]] = piece
            o_p = game.get_selected_piece()
            e = self.choose_extreme_piece()
            game.select(e)
            _,val = self.MinMax_place()
            if np.count_nonzero(game._board == -1) == 1:
                evaluations.append((place,-2))
            else:
                val= self.current_game_score()
                evaluations.append((place,val))
            game._board[place[0],place[1]] = -1
            game.select(o_p)
        game.select(piece)

        selected_place=0
        if isinstance(evaluations, list):
            selected_place = min(evaluations,key= lambda x:x[1])
        else:
            selected_place = evaluations
        return selected_place


    def place_piece(self) -> tuple[int, int]:
        game = self.get_game()
        if np.count_nonzero(game._board == -1)==1:
            for i in range(4):
                for j in range(4):
                    if game._board[i,j] ==-1:
                        return j,i
        
        p = self.MinMax_place()
        
        r=None
        if isinstance(p, tuple):
            r=p[0]
        else:
            r=p
        return r[1],r[0]
    
    def get_game(self):
        
        return super().get_game()
 
def main():
    game = quarto.Quarto()
    e= MinMaxPlayer(game)
    # # Making game easier for MinMax Algorithm to work 
    # # " Uncomment the next section and comment the ExpertPlayer line to test the MinMax "
    game.select(10)
    game.place(1,0)
    game.select(7)
    game.place(2,0)
    game.select(9)
    game.place(0,1)
    game.select(3)
    game.place(1,1)
    game.select(11)
    game.place(3,1)
    game.select(8)
    game.place(0,2)
    game.select(4)
    game.place(1,2)
    game.select(12)
    game.place(1,3)
    game.select(0)
    game.place(3,3)  
    game.set_players(( RandomPlayer(game),MinMaxPlayer(game)))

    # game.set_players((ExpertPlayer(game), RandomPlayer(game)))
    winner = game.run()
    logging.warning(f"main: Winner: player {winner}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count',
                        default=0, help='increase log verbosity')
    parser.add_argument('-d',
                        '--debug',
                        action='store_const',
                        dest='verbose',
                        const=2,
                        help='log debug messages (same as -vv)')
    args = parser.parse_args()

    if args.verbose == 0:
        logging.getLogger().setLevel(level=logging.WARNING)
    elif args.verbose == 1:
        logging.getLogger().setLevel(level=logging.INFO)
    elif args.verbose == 2:
        logging.getLogger().setLevel(level=logging.DEBUG)

    main()