using System.Data;

class Day20_1{
    public static void Run(){
        string[] lines = File.ReadAllLines(@"../../../src/inputs/input.txt");

        Dictionary<string, Module> modules = new Dictionary<string, Module>();
        foreach(string line in lines){
            string[] splitString = line.Split(" -> ");
            string[] connectedModules = splitString[1].Split(", ");
            if(splitString[0].Equals("broadcaster")){
                modules.Add("broadcaster", new Module('b', "broadcaster", connectedModules));
            } else {
                string name = splitString[0].Substring(1);
                char type = splitString[0].ToCharArray()[0];
                modules.Add(name, new Module(type, name, connectedModules));
            }
        }

        int highsignals = 0;
        int lowsignals = 0;
        Queue<(bool, string)> queuedSignals = new Queue<(bool, string)>();
        queuedSignals.Enqueue((false, "broadcaster"));
        while(queuedSignals.Count != 0){
            (bool currentSignal, string currentModuleName) = queuedSignals.Dequeue();
            Console.WriteLine(currentModuleName);
            Module currentModule = modules[currentModuleName];
            bool returnSignal = currentModule.sendSignal(currentSignal);
            foreach(string adjModule in currentModule.connectedModules){
                if(returnSignal){
                    highsignals++;
                } else {
                    lowsignals++;
                }

                queuedSignals.Enqueue((returnSignal, adjModule));
            }
        }

        Console.WriteLine(lowsignals + " " + highsignals + " " + lowsignals*highsignals);
    }


    public class Module {

        bool currentState;
        char type;
        public readonly string name;
        public readonly string[] connectedModules;

        public Module(char type, string name, string[] connectedModules){
            this.type = type;
            this.name = name;
            this.connectedModules = connectedModules;
            if(type == '%'){
                currentState = false;
            } else {
                currentState = true;
            }
        }


        public bool sendSignal(bool isHigh){
            if(this.type == '%'){
                currentState = !currentState;
                return currentState;
            } else if(this.type == '&'){
                if(isHigh && currentState){
                    return true;
                } else {
                    currentState = false;
                    return false;
                }
            } else {
                return isHigh;
            }
        }
    }
}