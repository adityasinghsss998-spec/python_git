class Developer{
  static raise_amt: number=1.05 // static
  name:string //instance variable
  pay:number;
  constructor(name:string,pay:number){
    this.name=name
    this.pay=pay
  }
  applyRaise():void{
    this.pay=Math.floor(this.pay*Developer.raise_amt)
  }
  static fromString(empStr:String):Developer{
    const [name,payStr]=empStr.split("-") //splits "Aditya-5000"
    return new Developer(name,parseInt(payStr,10));
  }
    
};

// so because typescipt and c++ uses a compiler and ompiler needs to know how much memory its going ot take and thats why they declare outside too but 
// python  an object is just a hidden hash map called __dict__ so we just inject keys at runtime so static comes under Developer.__dict__ adn instance in python is in seld.__dict__

class Manager extends Developer{
  teamsize:number;
  constructor(name:string,pay:number,teamsize:number){
    // this.teamSize = teamSize; // ❌ ERROR: 'this' is undefined here!
    super(name,pay);
    this.teamsize=teamsize
  }
}
