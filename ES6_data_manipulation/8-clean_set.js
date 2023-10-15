export default function cleanSet(inputSet, startString) {
  const resultArray = [];

  for (const value of inputSet) {
    if (value.startsWith(startString)) {
      resultArray.push(value.slice(startString.length));
    }
  }

  const resultString = resultArray.join('-');
  return resultString;
}
