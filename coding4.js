// @ts-check

// This program uses Node.js.
// To run this program, run this command: node coding4.js
// Explanation: This program uses a recursive algorithm to find the move
// for a player to take that will guarantee their win. For each possible move,
// it calls itself to figure out whether the other player can win if it plays
// that possible move next.
// Limitation: it can be very slow for large numbers of initial counters.

// AI

/**
 *
 * @param {number} n dividend
 * @param {number} m divisor
 * @returns {number} the remainder
 */
function remainder(n, m) {
  let ret = n % m;
  if (ret < 0) {
    ret += m;
  }
  return ret;
}

/**
 *
 * @param {number} numLeft total counters left
 * @param {number} remainderNeeded The remainder that I need to get
 * for my remaining counters
 * @returns {number | boolean} If I can't win, returns false. If
 * the game is over and I won, returns true. Otherwise, returns
 * the move I need to make in order to win.
 */
function moveNeeded(numLeft, remainderNeeded) {
  remainderNeeded = remainder(remainderNeeded, 2);
  if (numLeft === 0) {
    return remainderNeeded === 0;
  }
  for (let nextMove = 1; nextMove <= 3; nextMove++) {
    if (numLeft - nextMove < 0) {
      continue;
    }
    const newNumCounters = numLeft - nextMove;
    const newRemainderNeeded = remainder(remainderNeeded - nextMove, 2);
    const newRemainderOtherPlayerNeeds = remainder(
      newNumCounters + newRemainderNeeded + 1,
      2
    );
    const otherPlayerMoveNeeded = moveNeeded(
      newNumCounters,
      newRemainderOtherPlayerNeeds
    );

    if (otherPlayerMoveNeeded === false) {
      return nextMove;
    }
  }
  return false;
}

/**
 *
 * @param {number} numLeft total counters left
 * @param {number} numCountersAIHas Number of counters that the AI
 * has
 * @returns {number | boolean} If AI can't win, returns false. If
 * the game is over and AI won, returns true. Otherwise, returns
 * the move AI needs to make in order to win.
 */
function getAIMove(numLeft, numCountersAIHas) {
  return moveNeeded(numLeft, 1 - numCountersAIHas);
}

/**
 *
 * @param {number} numLeft total counters left
 * @param {number} numCountersAIHas Number of counters that the AI
 * has
 * @returns {number} The AI's next move
 */
function getFinalAIMove(numLeft, numCountersAIHas) {
  let ret = getAIMove(numLeft, numCountersAIHas);
  if (ret === false) {
    console.warn("I can't win. This is a bug.");
    ret = 1;
  } else if (ret === true) {
    console.warn("This is a bug.");
    ret = 1;
  }
  return ret;
}

/**
 *
 * @param {number} numCounters The initial total number of counters
 * @returns {boolean} Can the AI win?
 */
function shouldAIGoFirst(numCounters) {
  return getAIMove(numCounters, 0) !== false;
}

// GAME

const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

function question(query) {
  return new Promise((resolve) => {
    rl.question(query, resolve);
  });
}

let isComputerTurn = false;

let numCounters;
let numCountersHeld = { computer: 0, human: 0 };

async function main() {
  while (numCounters == null) {
    const answer = await question(
      "How many counters should we start with? Must be a positive odd integer. "
    );
    const int = parseInt(answer);
    if (typeof int === "number" && !isNaN(int) && int % 2 === 1) {
      numCounters = int;
    } else {
      console.log("That is not a positive odd integer");
    }
  }

  isComputerTurn = shouldAIGoFirst(numCounters);
  console.log((isComputerTurn ? "I'm" : "You're") + " going to go first.");

  while (numCounters > 0) {
    console.log((isComputerTurn ? "My" : "Your") + " turn!");
    let move;
    if (isComputerTurn) {
      move = getFinalAIMove(numCounters, numCountersHeld.computer);
      console.log(`I'm taking ${move} counters.`);
    } else {
      while (move == null) {
        const answer = await question(
          "How many counters will you take? Must be 1, 2, or 3. "
        );
        const int = parseInt(answer);

        if (![1, 2, 3].includes(int)) {
          console.log("Please input 1, 2, or 3.");
        } else if (numCounters - int < 0) {
          console.log(
            "There aren't enough counters for you to take that many!"
          );
        } else {
          move = int;
        }
      }
    }
    numCounters -= move;
    numCountersHeld[isComputerTurn ? "computer" : "human"] += move;
    isComputerTurn = !isComputerTurn;

    console.log(
      `There are ${numCounters} counters left. You have ${numCountersHeld.human}, and I have ${numCountersHeld.computer}.`
    );
  }

  if (numCountersHeld.computer % 2 === 1) {
    console.log("I won!");
  } else {
    console.log("You won!");
  }

  rl.close();
}

main();
