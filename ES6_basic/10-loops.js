export default function appendToEachArrayValue(inputArray, appendString) {
  const newArray = inputArray.map((value) => appendString + value);
  return newArray;
}
