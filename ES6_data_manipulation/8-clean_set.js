export default function cleanSet(inputSet, startString) {
  let resultString = '';
  if (!startString || !startString.length) return resultString;
  for (const element of inputSet) {
    if (element && element.startsWith(startString)) {
      resultString += `${element.slice(startString.length)}-`;
    }
  }
  return resultString.slice(0, resultString.length - 1);
}
