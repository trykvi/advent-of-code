using System.Xml.Schema;

class Day21_2 {

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

    public static int iterateBoard(char[][] board){
        List<Pos> OPositions = findAndClearOs(board);
        foreach(Pos position in OPositions){
            foreach(Pos adjPos in adjacentPositions(position)){
                if(IsWithinBounds(adjPos, 0, 0, board[0].Length, board.Length)){
                    if(board[adjPos.y][adjPos.x] != '#'){
                        board[adjPos.y][adjPos.x] = 'O';
                    }
                }
                
            }
        }

        return OPositions.Count;
        
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

    public static bool containsTwoTypes(Queue<int> numbers){
        if(numbers.Count < 10){
            return false;
        }
        int first = numbers.Dequeue();
        int second = numbers.Dequeue();
        foreach(int num in numbers){
            if(num != first && num != second){
                return false;
            }
        }

        return true;
    }

    public static char[][] duplicate(char[][] board, int xDupes, int yDupes){
        char[][] newBoard = new char[board.Length*yDupes][];
        for(int y = 0; y < newBoard.Length; y++){
            newBoard[y] = new char[board[0].Length*xDupes];
            for(int x = 0; x < newBoard[y].Length; x++){
                newBoard[y][x] = board[y % board.Length][x % board[0].Length];
            }
        }

        return newBoard;
    }

    public static char[][] getBoardWithinLimits(char[][] board, int x0, int y0, int width, int height){
        char[][] newBoard = new char[height][];
        for(int y = 0; y < newBoard.Length; y++){
            newBoard[y] = new char[width];
            for(int x = 0; x < newBoard[y].Length; x++){
                newBoard[y][x] = board[y0 + y][x0 + x];
            }
        }

        return newBoard;
    }
    public static void Run(){
        char[][] map = File.ReadAllLines(@"../../../src/inputs/input21.txt").Select(line => line.ToCharArray()).ToArray();
        char[][] expandedMap = duplicate(map, 5, 5);
        findAndClearOs(expandedMap);
        expandedMap[(expandedMap.Length+1)/2][(expandedMap[0].Length+1)/2] = 'S';

        int steps = 26_501_365;

        Queue<int> last10Nums = new Queue<int>();

        int iterations = 0;

        while(!containsTwoTypes(last10Nums)){
            int newNum = iterateBoard(map);
            if(last10Nums.Count < 10){
                last10Nums.Enqueue(newNum);
            } else {
                last10Nums.Dequeue();
                last10Nums.Enqueue(newNum);
            }
            iterations++;
        }

        int relevantSteps = (steps - (map.Length - 1) / 2) % map.Length + (map.Length - 1)/2;

        

        for(int i = 0; i < relevantSteps; i++){
            Console.WriteLine(iterateBoard(expandedMap));
            
        }

        for(int y = 0; y < expandedMap.Length; y++){
            for(int x = 0; x < expandedMap[y].Length; x++){
                if(expandedMap[y][x] == 'O'){
                    expandedMap[y][x] = 'O';
                }
            }
        }

        /* foreach(char[] line in expandedMap){
            Console.WriteLine(string.Join("", line));
        } */

        //Console.WriteLine(findAndClearOs(expandedMap).Count);

        int height = map.Length;
        int width = map[0].Length;

        

        foreach(char[] line in getBoardWithinLimits(expandedMap, width, 0, width, height)){
            Console.WriteLine(string.Join("", line));
        }

        long upCount1 = findAndClearOs(getBoardWithinLimits(expandedMap, 2*width, 0, width, height)).Count;
        long upCount2 = findAndClearOs(getBoardWithinLimits(expandedMap, 2*width, height, width, height)).Count;

        long rightCount1 = findAndClearOs(getBoardWithinLimits(expandedMap, 4*width, 2*height, width, height)).Count;
        long rightCount2 = findAndClearOs(getBoardWithinLimits(expandedMap, 3*width, 2*height, width, height)).Count;

        long downCount1 = findAndClearOs(getBoardWithinLimits(expandedMap, 2*width, 4*height, width, height)).Count;
        long downCount2 = findAndClearOs(getBoardWithinLimits(expandedMap, 2*width, 3*height, width, height)).Count;

        long leftCount1 = findAndClearOs(getBoardWithinLimits(expandedMap, 0, 2*height, width, height)).Count;
        long leftCount2 = findAndClearOs(getBoardWithinLimits(expandedMap, width, 2*height, width, height)).Count;


        long upperLeftCount1 = findAndClearOs(getBoardWithinLimits(expandedMap, 0, 0, width, height)).Count;
        long upperLeftCount2 = findAndClearOs(getBoardWithinLimits(expandedMap, 0, 0, width, height)).Count;

        long upperRightCount1 = findAndClearOs(getBoardWithinLimits(expandedMap, 2*width, 0, width, height)).Count;
        long upperRightCount2 = findAndClearOs(getBoardWithinLimits(expandedMap, 2*width, 0, width, height)).Count;

        long lowerLeftCount1 = findAndClearOs(getBoardWithinLimits(expandedMap, 0, 2*height, width, height)).Count;
        long lowerLeftCount2 = findAndClearOs(getBoardWithinLimits(expandedMap, 0, 2*height, width, height)).Count;

        long lowerRightCount1 = findAndClearOs(getBoardWithinLimits(expandedMap, 2*width, 2*height, width, height)).Count;
        long lowerRightCount2 = findAndClearOs(getBoardWithinLimits(expandedMap, 2*width, 2*height, width, height)).Count;

        long outfullDuplicates = (steps - ((width-1)/2) - relevantSteps) / width;
        long fullDuplicates = 2*outfullDuplicates*outfullDuplicates + 2*outfullDuplicates + 1;



        long innerOCount1 = last10Nums.Dequeue() * fullDuplicates;
        long innerOCount2 = last10Nums.Dequeue() * fullDuplicates;




        
    }

    public record Pos(int x, int y);
}