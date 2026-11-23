console.log("Скрипт архива кафедры загружен");

var groupmates = [
    {
        name: "Александр",
        surname: "Иванов",
        group: "БВТ1702",
        marks: [4, 3, 5]
    },
    {
        name: "Иван",
        surname: "Петров",
        group: "БСТ1702",
        marks: [4, 4, 4]
    },
    {
        name: "Кирилл",
        surname: "Смирнов",
        group: "БАП1801",
        marks: [5, 5, 5]
    }
];

console.log(groupmates);

function rpad(value, width) {
    let text = String(value);
    while (text.length < width) {
        text += " ";
    }
    return text;
}

function printStudents(students) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 10),
        "Оценки"
    );

    for (const student of students) {
        console.log(
            rpad(student.name, 15),
            rpad(student.surname, 15),
            rpad(student.group, 10),
            student.marks.join(", ")
        );
    }
}

printStudents(groupmates);

function filterStudentsByGroup(students, groupName) {
    const group = groupName.trim().toUpperCase();
    return students.filter(student => student.group.toUpperCase() === group);
}

const groupName = prompt("Введите название группы:");

if (groupName !== null && groupName.trim() !== "") {
    const result = filterStudentsByGroup(groupmates, groupName);
    console.log("Результат поиска по группе:", groupName.trim());

    if (result.length > 0) {
        printStudents(result);
    } else {
        console.log("Студентов такой группы нет.");
    }
}

function filterStudentsByAverage(students, threshold) {
    return students.filter(student => {
        const marks = student.marks;
        if (marks.length === 0) {
            return false;
        }

        const sum = marks.reduce((total, mark) => total + mark, 0);
        const average = sum / marks.length;
        return average > threshold;
    });
}

const thresholdInput = prompt("Введите порог среднего балла:");

if (thresholdInput !== null) {
    const input = thresholdInput.trim().replace(",", ".");
    const threshold = Number(input);

    if (input === "" || !Number.isFinite(threshold)) {
        console.log("Введите числовое значение порога.");
    } else {
        const result = filterStudentsByAverage(groupmates, threshold);
        console.log("Студенты со средним баллом выше", threshold);

        if (result.length > 0) {
            printStudents(result);
        } else {
            console.log("Студентов с таким средним баллом нет.");
        }
    }
}