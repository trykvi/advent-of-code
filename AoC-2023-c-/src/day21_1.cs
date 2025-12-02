class Day21_1 {

    public static List<Pos> findAndClearOs(char[][] board){
        List<Pos> OPositions = new List<Pos>();
        for(int y = 0; y < board.Length; y++){
            for(int x = 0; x < board.Length; x++){
                if(IsWithinBounds(new Pos(x, y), 0, 0, board[0].Length, board.Length)){
                    if(board[y][x] == 'O' || board[y][x] == 'S'){
                        OPositions.Add(new Pos(x, y));
                        board[y][x] = '.';
                    }
                }
                
            }
        }

        return OPositions;
    }

    public static Pos[] adjacentPositions(Pos pos){
        int x = pos.x;
        int y = pos.y;
        return new Pos[]{
            new Pos(x-1, y),
            new Pos(x+1, y),
            new Pos(x, y+1),
            new Pos(x, y-1)
        };
    }

    public static void iterateBoard(char[][] board){
        List<Pos> OPositions = findAndClearOs(board);
        foreach(Pos position in OPositions){
            foreach(Pos adjPos in adjacentPositions(position)){
                if(board[adjPos.y][adjPos.x] != '#'){
                    board[adjPos.y][adjPos.x] = 'O';
                }
            }
        }
        
    }

    public static Boolean IsWithinBounds(Pos pos, int x0, int y0, int x1, int y1){
        if(pos.x < x0){
            return false;
        }

        if(pos.x >= x1){
            return false;
        }

        if(pos.y < y0){
            return false;
        }

        if(pos.y >= y1){
            return false;
        }

        return true;
    }
    public static void Run(){
        char[][] map = File.ReadAllLines(@"../../../src/inputs/input21.txt").Select(line => line.ToCharArray()).ToArray();

        for(int i = 0; i < 64; i++){
            iterateBoard(map);
        }

        Console.WriteLine(findAndClearOs(map).Count);
    }

    public record Pos(int x, int y);
}