#!/usr/bin/node
const args = process.argv.slice(2);

// If no arguments or only one argument is passed, print 0
if (args.length <= 1) {
  console.log(0);
} else {
  // Convert all arguments to numbers and store them in an array
  const nums = args.map(Number);

  // Sort the array in descending order
  nums.sort((a, b) => b - a);

  // Print the second element in the sorted array (the second biggest)
  console.log(nums[1]);
}
