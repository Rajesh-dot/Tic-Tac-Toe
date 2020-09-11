import java.util.*;
public class TicTacToe{
	static char[] board = new char[10];
	public static void main(String[] args) {
		//static char[] board = new String[10];
		for(int i=0;i<10;i++){
			board[i]=' ';
		}
		prints("Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical). The board has positions 1-9 starting at the top left.");
		printBoard(board);
		while(!isBoardFull(board)){
			if(!isWinner(board,'O')){
				playerMove();
				printBoard(board);
			}
			else{
				prints("O's win this time...");
				break;
			}
			if(!isWinner(board,'X')){
				int move=compMove();
				if(move==0){
					prints("Game is Tie!");
				}
				else{
					insertLetter('O',move);
					prints("Computer placed an 'O' in position");
					printBoard(board);
				}
			}
			else{
				prints("X is won");
				break;
			}
		}
		if(isBoardFull(board)){
			prints("Tie game!");
		}
	}
	static void insertLetter(char letter,int pos){
		board[pos]=letter;
	}
	static boolean spaceIsFree(int pos){
		return board[pos]==' ';
	}
	static void printBoard(char[] board){
		prints("   |   |");
    	prints(" "+board[1] + " | " + board[2] + " | " + board[3]);
    	prints("   |   |");
    	prints("-----------");
    	prints("   |   |");
    	prints(" " + board[4] + " | " + board[5] + " | " + board[6]);
    	prints("   |   |");
    	prints("-----------");
    	prints("   |   |");
    	prints(" " + board[7] + " | " + board[8] + " | " + board[9]);
    	prints("   |   |");
    	prints(" ");
	}
	static void prints(String st){
		System.out.println(st);
	}
	static boolean isWinner(char[] bo, char le){
	    return ((bo[7] == le && bo[8] == le && bo[9] == le) ||  //across the top
		(bo[4] == le && bo[5] == le && bo[6] == le) ||  //across the middle
		(bo[1] == le && bo[2] == le && bo[3] == le) ||  //across the bottom
		(bo[7] == le && bo[4] == le && bo[1] == le) || //down the left side
		(bo[8] == le && bo[5] == le && bo[2] == le) || //down the middle
		(bo[9] == le && bo[6] == le && bo[3] == le) || //down the right side
		(bo[7] == le && bo[5] == le && bo[3] == le) || //diagonal
		(bo[9] == le && bo[5] == le && bo[1] == le)); //diagonal
	}
	static boolean isBoardFull(char[] board){
		int c=0;
		for(int i=0;i<10;i++){
			if (board[i]==' '){
				c+=1;
			}
		}
		if(c>1){
			return false;
		}
		else{
			return true;
		}
	}
	static void playerMove(){
		boolean run=true;
		Scanner s=new Scanner(System.in);
		while(run){
		    prints("enter your move");
			int move=s.nextInt();
			try{
				if(move>0 && move<10){
					if(spaceIsFree(move)){
						run=false;
						insertLetter('X',move);
					}
					else{
						prints("This position is already occupied");
					}
				}
				else{
					prints("Please type with in the range");
				}
			}
			catch(Exception e){
				prints("Please type a number!");
			}
		}
	}
	static int compMove(){
		/*
		int[] possibleMoves=new int[10];
		for(int i=0;i<10;i++){
			possibleMoves[i]=0;
		}
		*/
		List<Integer> possibleMoves = new ArrayList<Integer>(10); 
		for(int i=1;i<10;i++){
			if(board[i]==' '){
				possibleMoves.add(i);
			}
		}
		int move=0;
		char[] xo = new char[2];
		xo[0]='O';
		xo[1]='X';
		char[] boardcopy = new char[10];
		for(char let:xo){
			for(int i:possibleMoves){
				for(int j=0;j<10;j++){
					boardcopy[j]=board[j];
				}
				boardcopy[i]=let;
				if(isWinner(boardcopy,let)){
					move=i;
					return move;
				}
			}
		}
		List<Integer> cornersOpen = new ArrayList<Integer>(10);
		for(int i:possibleMoves){
			if(i==1 || i==3 || i==7 || i==9){
				cornersOpen.add(i);
			}
		}
		int size = cornersOpen.size();
		if(size>0){
			move=selectRandom(cornersOpen);
			return move;
		}
		for(int i:possibleMoves){
			if(i==5){
				move=5;
				return move;
			}
		}
		List<Integer> edgesOpen = new ArrayList<Integer>(10);
		for(int i:possibleMoves){
			if(i==2 || i==4 || i==6 || i==8){
				edgesOpen.add(i);
			}
		}
		int size2 = edgesOpen.size();
		if(size2>0){
			move=selectRandom(edgesOpen);
		}
		return move;
	}
	static int selectRandom(List<Integer> li){
		Random rand = new Random(); 
        return li.get(rand.nextInt(li.size())); 
	}
	static int score(char[] board){
		if(isWinner(board,'O')){
			return 10;
		}
		if(isWinner(board,'X')){
			return -10;
		}
		if(isBoardFull(board)){
			return 0;
		}
		return 0;
	}
}