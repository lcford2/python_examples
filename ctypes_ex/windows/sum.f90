! filename = sum.f90
! Purpose: To be used as a shared library 

! Function to sum two real valued numbers
FUNCTION sum(x,y) 
    !DEC$ ATTRIBUTES DLLEXPORT :: sum
    double precision :: sum
    double precision, intent(in) :: x, y
        
    sum = x+y
END FUNCTION sum

! Subroutine to add two real valued numbers
SUBROUTINE sum_sub(x,y,output)
    !DEC$ ATTRIBUTES DLLEXPORT :: sum_sub
    double precision, intent(in) :: x, y
    double precision, intent(out) :: output

    output = x+y
END SUBROUTINE sum_sub

! function to calculate average of array of doubles
FUNCTION average(length, values)
    !DEC$ ATTRIBUTES DLLEXPORT :: average
    integer, intent(in) :: length
    double precision, intent(in) :: values(length)
    double precision :: average
    
    average = 0.0
    DO i = 1, length
        average = average + values(i)
    ENDDO
    average = average/length
END FUNCTION average
