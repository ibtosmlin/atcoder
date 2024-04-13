import * as fs from "fs";

const inputs = fs.readFileSync("/dev/stdin", "utf8").split("\n");
const N = Number(inputs[0]);
const A = inputs[1].split(" ").map(Number);
const [N, M] = inputs[1].split(" ").map(Number);

function main(){
    const count = Array(101).fill(0);
    for (let i = 0; i < A.length; i++) {
        count[A[i]] += 1;
    }
    for (let i = 0; i <= 100; i++) {
        if (count[i] > 0 &&  count[i] <= 10){
            console.log('Yes');
            return 0;
        }
    }
    console.log('No');
    return 0;
    };

main();