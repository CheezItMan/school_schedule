import pytest
from school_schedule.student import Student


# Constructor Tests

# Nominal 

# Create new_student = Student("Saharai", 10, ["Math"])
# Make sure new_student has the proper name, grade and classes

def test_can_create_nominal_student():
    # Arrange

    # Act
    new_student = Student("Saharai", 10, ["Math"])

    # Assert
    assert new_student.name == "Saharai"
    assert new_student.grade == 10
    assert len(new_student.classes) == 1
    assert "Math" in new_student.classes



# Edge Case
# Create new_student = Student("Saharai", 10, [])
# Make sure new_student has the proper name, grade and classes
def test_can_create_student_with_no_classes():
    # Arrange

    # Act
    new_student = Student("Saharai", 10, [])

    # Assert
    assert new_student.name == "Saharai"
    assert new_student.grade == 10
    assert len(new_student.classes) == 0



# add_class Tests
# Nominal
# We can new_student.add_class(Basketweaving) when the student doesn't already
#    have physics

def test_add_class_to_student():
    # Arrange
    new_student = Student("Saharai", 10, [])

    # Act
    new_student.add_class("Basketweaving")

    # Assert
    assert len(new_student.classes) == 1
    assert "Basketweaving" in new_student.classes


# Edge Case
# We can new_student.add_class(“Physics”) when the student already
#    has physics.  In this case... we raise an error
# **Optional** We could add a list of classes

# Arrange
    new_student = Student("Saharai", 10, ["Basketweaving"])

    # Act-Assert
    with pytest.raises(Exception):
        new_student.add_class("Basketweaving")

# get_num_classes
# Nominal
# The number of classes increases by 1 if we add a class

# Edge
# 0 when there are no classes

# summary
# We can call the function and it doesn't break