// Sample Data
import fs from "fs";

interface lecture {
  id: number;
  code: string;
  name: string;
  instructor: string;
  classGroup: string;
  room: string;
  duration: number;
}

const loadSampleData = async () => {
  const data = await fs.promises.readFile("lecturesData.json", "utf-8");
  return JSON.parse(data);
};

(async () => {
  const lecturesData: lecture[] = await loadSampleData();

  // Adjacency Lists
  let conflictingLists: lecture[][] = [];

  for (let i = 0; i < lecturesData.length; i++) {
    console.log(lecturesData[0].code);
    let tempAdjacencyList: lecture[] = [];
    for (let j = 0; j < lecturesData.length; j++) {
      if (i != j) {
        const currentLecture = lecturesData[i];
        const conflictingCandidate = lecturesData[j];
        if (
          currentLecture.instructor === conflictingCandidate.instructor ||
          currentLecture.classGroup === currentLecture.classGroup
        ) {
          tempAdjacencyList.push(conflictingCandidate);
        }
      }
    }
    conflictingLists.push(tempAdjacencyList);
  }

  console.log(conflictingLists[0]);
})();
