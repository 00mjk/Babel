! 
! File:          vect_Utils_Impl.F90
! Symbol:        vect.Utils-v1.0
! Symbol Type:   class
! Babel Version: 2.0.0 (Revision: 7463M trunk)
! Description:   Server-side implementation for vect.Utils
! 
! WARNING: Automatically generated; only changes within splicers preserved
! 
! 


! 
! Symbol "vect.Utils" (version 1.0)
! 


#include "vect_Utils_fAbbrev.h"
#include "vect_vNegValExcept_fAbbrev.h"
#include "sidl_PostViolation_fAbbrev.h"
#include "vect_BadLevel_fAbbrev.h"
#include "sidl_RuntimeException_fAbbrev.h"
#include "sidl_ClassInfo_fAbbrev.h"
#include "sidl_BaseClass_fAbbrev.h"
#include "sidl_BaseInterface_fAbbrev.h"
#include "vect_vDivByZeroExcept_fAbbrev.h"
#include "sidl_PreViolation_fAbbrev.h"
#include "sidl_BaseException_fAbbrev.h"
! DO-NOT-DELETE splicer.begin(_miscellaneous_code_start)
#include "sidl_SIDLException_fAbbrev.h"

  subroutine getInfo(a, lowA, lenA)
  use sidl_double_array
  implicit none
  type(sidl__array), intent(in)        :: a
  integer (kind=sidl_int), intent(out) :: lenA, lowA
  integer (kind=sidl_int)              :: dimA, upA
  type(sidl_double_1d)                 :: a1

  call cast(a, a1)
  if (not_null(a1)) then
    dimA = dimen(a1)
    lowA = lower(a1, 0_sidl_int)
    upA  = upper(a1, 0_sidl_int)
    lenA = (upA - lowA) + 1_sidl_int
  else
     lenA = -1 * 1_sidl_int
  endif

  return
  end

  subroutine createArray(lenA, a)
    use sidl_double_array
    implicit none
    integer (kind=sidl_int), intent(in) :: lenA
    type(sidl__array), intent(out)      :: a
    type(sidl_double_1d)                :: tmp

    if (lenA .gt. 0_sidl_int) then
       call create1d(lenA, tmp)
       call cast(tmp, a)
    else
       call set_null(tmp)
       call cast(tmp, a)
    endif

    return
  end subroutine createArray

  subroutine createMatrix(lenA, a)
    use sidl_double_array
    implicit none
    integer (kind=sidl_int), intent(in) :: lenA
    type(sidl__array), intent(out)      :: a
    type(sidl_double_2d)                :: tmp

    if (lenA .gt. 0_sidl_int) then
       call create2dCol(lenA, lenA, tmp)
       call cast(tmp, a)
    else
       call set_null(tmp)
       call cast(tmp, a)
    endif

    return
  end subroutine createMatrix
! DO-NOT-DELETE splicer.end(_miscellaneous_code_start)



! 
! Method:  _ctor[]
! Class constructor called when the class is created.
! 

recursive subroutine vect_Utils__ctor_mi(self, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_Utils
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils._ctor.use)
  ! Nothing needed here.
  ! DO-NOT-DELETE splicer.end(vect.Utils._ctor.use)
  implicit none
  type(vect_Utils_t) :: self
  ! in
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils._ctor)
! Nothing needed here.
! DO-NOT-DELETE splicer.end(vect.Utils._ctor)
end subroutine vect_Utils__ctor_mi


! 
! Method:  _ctor2[]
! Special Class constructor called when the user wants to wrap his own private data.
! 

recursive subroutine vect_Utils__ctor2_mi(self, private_data, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_Utils
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils._ctor2.use)
  ! Nothing needed here.
  ! DO-NOT-DELETE splicer.end(vect.Utils._ctor2.use)
  implicit none
  type(vect_Utils_t) :: self
  ! in
  type(vect_Utils_wrap) :: private_data
  ! in
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils._ctor2)
! Nothing needed here.
! DO-NOT-DELETE splicer.end(vect.Utils._ctor2)
end subroutine vect_Utils__ctor2_mi


! 
! Method:  _dtor[]
! Class destructor called when the class is deleted.
! 

recursive subroutine vect_Utils__dtor_mi(self, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_Utils
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils._dtor.use)
  ! Nothing needed here
  ! DO-NOT-DELETE splicer.end(vect.Utils._dtor.use)
  implicit none
  type(vect_Utils_t) :: self
  ! in
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils._dtor)
! Nothing needed here.
! DO-NOT-DELETE splicer.end(vect.Utils._dtor)
end subroutine vect_Utils__dtor_mi


! 
! Method:  _load[]
! Static class initializer called exactly once before any user-defined method is dispatched
! 

recursive subroutine vect_Utils__load_mi(exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_Utils
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils._load.use)
  ! Nothing needed here.
  ! DO-NOT-DELETE splicer.end(vect.Utils._load.use)
  implicit none
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils._load)
! Nothing needed here.
! DO-NOT-DELETE splicer.end(vect.Utils._load)
end subroutine vect_Utils__load_mi


! 
! Method:  vuIsZero[]
! boolean result operations 
! Return TRUE if the specified vector is the zero vector, within the
! given tolerance level; otherwise, return FALSE.
! 

recursive subroutine vect_Utils_vuIsZero_mi(u, tol, retval, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_Utils
  use sidl_PreViolation
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuIsZero.use)
  use sidl_double_array
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuIsZero.use)
  implicit none
  type(sidl__array) :: u
  ! in
  real (kind=sidl_double) :: tol
  ! in
  logical :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuIsZero)
  integer (kind=sidl_int) :: lowU, lenU, i
  real (kind=sidl_double) :: val
  type(sidl_double_1d)    :: du
  call cast(u, du)

  call getInfo(u, lowU, lenU)
  if (lenU .gt. 0_sidl_int) then
     retval = .true.
     i = 0_sidl_int
     do while ( retval .and. (i .lt. lenU) )
        call get(du, lowU+i, val)
        if (ABS(val) .gt. ABS(tol)) then
           retval = .false.
        endif
        i = i + 1_sidl_int
     enddo
  else
     retval = .false.
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuIsZero)
end subroutine vect_Utils_vuIsZero_mi


! 
! Method:  vuIsUnit[]
! Return TRUE if the specified vector is the unit vector, within the
! given tolerance level; otherwise, return FALSE.
! 

recursive subroutine vect_Utils_vuIsUnit_mi(u, tol, retval, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_Utils
  use sidl_PreViolation
  use vect_vNegValExcept
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuIsUnit.use)
  use sidl_SIDLException
  use vect_BadLevel
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuIsUnit.use)
  implicit none
  type(sidl__array) :: u
  ! in
  real (kind=sidl_double) :: tol
  ! in
  logical :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuIsUnit)
  real (kind=sidl_double)    :: val
  type(sidl_SIDLException_t) :: sExcept
  type(sidl_BaseInterface_t) :: throwaway_exception
  character (len=20)         :: myfilename
  character (len=22)         :: myname

  myfilename = 'vect_Utils_Impl.f'
  myname     = 'vect_Utils_vuIsUnit'

  if (not_null(u)) then
     call vect_Utils_vuNorm_mi(u, tol, NoVio, val, exception)
     if (is_null(exception)) then
        if (ABS(val - 1.0_sidl_double) .le. ABS(tol)) then
           retval = .true.
        else
           retval = .false.
        endif
     else
        retval = .false.
        call cast(exception, sExcept, throwaway_exception)
        if (not_null(sExcept)) then
           call add(sExcept, myfilename, 295_sidl_int, myname, &
                    throwaway_exception)
           call deleteRef(sExcept, throwaway_exception)
           return
        endif
     endif
  else
     retval = .false.
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuIsUnit)
end subroutine vect_Utils_vuIsUnit_mi


! 
! Method:  vuAreEqual[]
! Return TRUE if the specified vectors are equal, within the given
! tolerance level; otherwise, return FALSE.
! 

recursive subroutine vect_Utils_vuAreEqual_mi(u, v, tol, retval, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_Utils
  use sidl_PreViolation
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuAreEqual.use)
  use sidl_double_array
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuAreEqual.use)
  implicit none
  type(sidl__array) :: u
  ! in
  type(sidl__array) :: v
  ! in
  real (kind=sidl_double) :: tol
  ! in
  logical :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuAreEqual)
  integer (kind=sidl_int) :: i, lenU, lenV, lowU, lowV
  real (kind=sidl_double) :: ui, vi
  type(sidl_double_1d)    :: du
  type(sidl_double_1d)    :: dv
  call cast(u, du)
  call cast(v, dv)

  if ( (not_null(u)) .and. (not_null(v)) ) then
     call getInfo(u, lowU, lenU)
     call getInfo(v, lowV, lenV)
     if ( (lenU .gt. 0_sidl_int) .and. (lenU .eq. lenV) ) then
        retval = .true.
        i = 0_sidl_int
        do while ( retval .and. (i .lt. lenU) )
           call get(du, lowU+i, ui)
           call get(dv, lowV+i, vi)
           if (ABS(ui - vi) .gt. ABS(tol)) then
              retval = .false.
           endif
           i = i + 1_sidl_int
        enddo
     else
        retval = .false.
     endif
  else if ( (is_null(u)) .and. (is_null(v)) ) then
!    Is this even appropriate/valid?
     retval = .true.
  else
     retval = .false.
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuAreEqual)
end subroutine vect_Utils_vuAreEqual_mi


! 
! Method:  vuAreOrth[]
! Return TRUE if the specified vectors are orthogonal, within the given
! tolerance; otherwise, return FALSE.
! 

recursive subroutine vect_Utils_vuAreOrth_mi(u, v, tol, retval, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_Utils
  use sidl_PreViolation
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuAreOrth.use)
  use sidl_SIDLException
  use vect_BadLevel
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuAreOrth.use)
  implicit none
  type(sidl__array) :: u
  ! in
  type(sidl__array) :: v
  ! in
  real (kind=sidl_double) :: tol
  ! in
  logical :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuAreOrth)
  real (kind=sidl_double)    :: val
  type(sidl_SIDLException_t) :: sExcept
  type(sidl_BaseInterface_t) :: throwaway_exception
  character (len=20)         :: myfilename
  character (len=23)         :: myname

  myfilename = 'vect_Utils_Impl.f'
  myname     = 'vect_Utils_vuAreOrth'

  if ( not_null(u) .and. not_null(v) ) then
     call vect_Utils_vuDot_mi(u, v, tol, NoVio, val, exception)
     if (is_null(exception)) then
        if (ABS(val) .le. ABS(tol)) then
          retval = .true.
        else
          retval = .false.
        endif
     else
        retval = .false.
        call cast(exception, sExcept, throwaway_exception)
        if (not_null(sExcept)) then
           call add(sExcept, myfilename, 413_sidl_int, myname, &
                    throwaway_exception)
           call deleteRef(sExcept, throwaway_exception)
           return
        endif
     endif
  else
     retval = .false.
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuAreOrth)
end subroutine vect_Utils_vuAreOrth_mi


! 
! Method:  vuSchwarzHolds[]
! Return TRUE if the Schwarz (or Cauchy-Schwarz) inequality holds, within
! the given tolerance; otherwise, return FALSE.
! 

recursive subroutine vect_Utils_vuSchwarzHolds_mi(u, v, tol, retval,           &
  exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_Utils
  use sidl_PreViolation
  use vect_vNegValExcept
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuSchwarzHolds.use)
  use sidl_SIDLException
  use vect_BadLevel
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuSchwarzHolds.use)
  implicit none
  type(sidl__array) :: u
  ! in
  type(sidl__array) :: v
  ! in
  real (kind=sidl_double) :: tol
  ! in
  logical :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuSchwarzHolds)
  real (kind=sidl_double)    :: valDot, valNormU, valNormV, val
  type(sidl_SIDLException_t) :: sExcept
  type(sidl_BaseInterface_t) :: throwaway_exception
  character (len=20)         :: myfilename
  character (len=27)         :: myname

  myfilename = 'vect_Utils_Impl.f'
  myname     = 'vect_Utils_vuSchwarzHolds'

  if ( not_null(u) .and. not_null(v) ) then
     call vect_Utils_vuDot_mi(u, v, tol, NoVio, valDot, exception)
     if (is_null(exception)) then
        call vect_Utils_vuNorm_mi(u, tol, NoVio, valNormU, exception)
        if (is_null(exception)) then
           call vect_Utils_vuNorm_mi(v, tol, NoVio, valNormV, exception)
           if (is_null(exception)) then
              val = valNormU * valNormV
              if (ABS(valDot) .le. ABS(val) + ABS(tol)) then
                retval = .true.
              else
                retval = .false.
              endif
           else
              retval = .false.
              call cast(exception, sExcept, throwaway_exception)
              if (not_null(sExcept)) then
                 call add(sExcept, myfilename, 482_sidl_int, myname, &
                          throwaway_exception)
                 call deleteRef(sExcept, throwaway_exception)
                return
              endif
           endif
        else
           retval = .false.
           call cast(exception, sExcept, throwaway_exception)
           if (not_null(sExcept)) then
              call add(sExcept, myfilename, 497_sidl_int, myname, &
                       throwaway_exception)
              call deleteRef(sExcept, throwaway_exception)
              return
           endif
        endif
     else
        retval = .false.
        call cast(exception, sExcept, throwaway_exception)
        if (not_null(sExcept)) then
           call add(sExcept, myfilename, 476_sidl_int, myname, &
                    throwaway_exception)
           call deleteRef(sExcept, throwaway_exception)
           return
        endif
     endif
  else
     retval = .false.
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuSchwarzHolds)
end subroutine vect_Utils_vuSchwarzHolds_mi


! 
! Method:  vuTriIneqHolds[]
! Return TRUE if the Minkowski (or triangle) inequality holds, within the
! given tolerance; otherwise, return FALSE.
! 

recursive subroutine vect_Utils_vuTriIneqHolds_mi(u, v, tol, retval,           &
  exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_Utils
  use sidl_PreViolation
  use vect_vNegValExcept
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuTriIneqHolds.use)
  use sidl_SIDLException
  use vect_BadLevel
  use sidl_double_array
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuTriIneqHolds.use)
  implicit none
  type(sidl__array) :: u
  ! in
  type(sidl__array) :: v
  ! in
  real (kind=sidl_double) :: tol
  ! in
  logical :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuTriIneqHolds)
  real (kind=sidl_double)    :: valSum, sumNorm, valNormU, valNormV, normTot
  type(sidl_SIDLException_t) :: sExcept
  type(sidl_BaseInterface_t) :: throwaway_exception
  type(sidl__array)          :: aSum
  character (len=20)         :: myfilename
  character (len=28)         :: myname

  myfilename = 'vect_Utils_Impl.f'
  myname     = 'vect_Utils_vuTriIneqHolds'

  call set_null(aSum)
  if ( (not_null(u)) .and. (not_null(v)) ) then
     call vect_Utils_vuSum_mi(u, v, NoVio, aSum, exception)
     if (is_null(exception)) then
        call vect_Utils_vuNorm_mi(aSum, tol, NoVio, sumNorm, exception)
        if (is_null(exception)) then
           call vect_Utils_vuNorm_mi(u, tol, NoVio, valNormU, exception)
           if (is_null(exception)) then
              call vect_Utils_vuNorm_mi(v, tol, NoVio, valNormV, &
                                        exception)
              if (is_null(exception)) then
                 normTot = ABS(valNormU + valNormV) + ABS(tol)
                 if ( ABS(sumNorm) .le. ABS(normTot) ) then
                   retval = .true.
                 else
                   retval = .false.
                 endif
              else
                 retval = .false.
                 call cast(exception, sExcept, throwaway_exception)
                 if (not_null(sExcept)) then
                    call add(sExcept, myfilename, 563_sidl_int, &
                             myname, throwaway_exception)
                    call deleteRef(sExcept, throwaway_exception)
                    return
                 endif
              endif
           else
              retval = .false.
              call cast(exception, sExcept, throwaway_exception)
              if (not_null(sExcept)) then
                 call add(sExcept, myfilename, 560_sidl_int, myname, &
                          throwaway_exception)
                 call deleteRef(sExcept, throwaway_exception)
                 return
              endif
           endif
        else
           retval = .false.
           call cast(exception, sExcept, throwaway_exception)
           if (not_null(sExcept)) then
              call add(sExcept, myfilename, 557_sidl_int, myname, &
                       throwaway_exception)
              call deleteRef(sExcept, throwaway_exception)
           endif
        endif
     else
        retval = .false.
        call cast(exception, sExcept, throwaway_exception)
        if (not_null(sExcept)) then
           call add(sExcept, myfilename, 555_sidl_int, myname, &
                    throwaway_exception)
           call deleteRef(sExcept, throwaway_exception)
           return
        endif
     endif
  else
     retval = .false.
  endif

  if (not_null(aSum)) then 
    call deleteRef(aSum)
  endif
  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuTriIneqHolds)
end subroutine vect_Utils_vuTriIneqHolds_mi


! 
! Method:  vuNorm[]
! double result operations 
! Return the norm (or length) of the specified vector.
! 
! Note that the size exception is given here simply because the
! implementation is leveraging the vuDot() method.  Also the tolerance
! is included to enable the caller to specify the tolerance used in
! contract checking.
! 

recursive subroutine vect_Utils_vuNorm_mi(u, tol, badLevel, retval, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_BadLevel
  use vect_Utils
  use sidl_PostViolation
  use sidl_PreViolation
  use vect_vNegValExcept
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuNorm.use)
  use sidl_SIDLException
  use vect_BadLevel
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuNorm.use)
  implicit none
  type(sidl__array) :: u
  ! in
  real (kind=sidl_double) :: tol
  ! in
  integer (kind=sidl_enum) :: badLevel
  ! in
  real (kind=sidl_double) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuNorm)
  real (kind=sidl_double)      :: valDot
  type(sidl_SIDLException_t)   :: sExcept
  type(vect_vNegValExcept_t) :: negValExcept
  type(sidl_BaseInterface_t)   :: throwaway_exception
  character (len=20)           :: myfilename
  character (len=20)           :: myname
  character (len=80)           :: msg
  
  myfilename = 'vect_Utils_Impl.f'
  myname     = 'vect_Utils_vuNorm'
  msg        = 'vuNorm: vNegValExcept: Cannot sqrt() a negative value.'

  if (badLevel .eq. NoVio) then
     if (not_null(u)) then
        call vect_Utils_vuDot_mi(u, u, tol, NoVio, valDot, exception)
        if (is_null(exception)) then
           if (valDot .gt. 0.0_sidl_double) then
             retval = sqrt(valDot)
           else if (valDot .eq. 0.0_sidl_double) then
             retval = 0.0_sidl_double
           else
!            This should NEVER happen!
             retval = -1.0 * 5.0_sidl_double
             call new(negValExcept, throwaway_exception)
              if (not_null(exception)) then
                call setNote(negValExcept, msg, throwaway_exception)
                call add(negValExcept, myfilename, 663_sidl_int, &
                         myname, throwaway_exception)
                call cast(negValExcept, exception, throwaway_exception)
                call deleteRef(negValExcept, throwaway_exception)
                return
              endif
           endif
        else
           retval = -1.0 * 5.0_sidl_double
           call cast(exception, sExcept, throwaway_exception)
           if (not_null(sExcept)) then
              call add(sExcept, myfilename, 663_sidl_int, myname, &
                       throwaway_exception)
              call deleteRef(sExcept, throwaway_exception)
              return
           endif
        endif
     else
        retval = 0.0_sidl_double
     endif
  else if (badLevel .eq. NegRes) then
     retval = -1.0 * 5.0_sidl_double
  else if (badLevel .eq. PosRes) then
     retval = 5.0_sidl_double
  else if (badLevel .eq. ZeroRes) then
     retval = 0.0_sidl_double
  else
     retval = -1.0 * 5.0_sidl_double
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuNorm)
end subroutine vect_Utils_vuNorm_mi


! 
! Method:  vuDot[]
! Return the dot (, inner, or scalar) product of the specified vectors.
! 

recursive subroutine vect_Utils_vuDot_mi(u, v, tol, badLevel, retval,          &
  exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_BadLevel
  use vect_Utils
  use sidl_PostViolation
  use sidl_PreViolation
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuDot.use)
  use vect_BadLevel
  use sidl_double_array
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuDot.use)
  implicit none
  type(sidl__array) :: u
  ! in
  type(sidl__array) :: v
  ! in
  real (kind=sidl_double) :: tol
  ! in
  integer (kind=sidl_enum) :: badLevel
  ! in
  real (kind=sidl_double) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuDot)
  integer (kind=sidl_int) :: i, lenU, lenV, lowU, lowV
  real (kind=sidl_double) :: ui, vi
  type(sidl_double_1d)    :: du
  type(sidl_double_1d)    :: dv
  call cast(u, du)
  call cast(v, dv)

  if (badLevel .eq. NoVio) then
     if ( not_null(u) .and. not_null(v) ) then
        call getInfo(u, lowU, lenU)
        call getInfo(v, lowV, lenV)
        if ( (lenU .gt. 0_sidl_int) .and. (lenU .eq. lenV) ) then
           retval = 0.0_sidl_double
           do i = 0_sidl_int, lenU - 1_sidl_int
              call get(du, lowU+i, ui)
              call get(dv, lowV+i, vi)
              retval = retval + (ui * vi)
           enddo
        else
           retval = 0.0_sidl_double
        endif
     else
        retval = 0.0_sidl_double
     endif
  else if (badLevel .eq. NegRes) then
     retval = -1.0 * 5.0_sidl_double
  else if (badLevel .eq. PosRes) then
     retval = 5.0_sidl_double
  else
     retval = -1.0 * 1.0_sidl_double
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuDot)
end subroutine vect_Utils_vuDot_mi


! 
! Method:  vuProduct[]
! vector result operations 
! Return the (scalar) product of the specified vector.
! 

recursive subroutine vect_Utils_vuProduct_mi(a, u, badLevel, retval,           &
  exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_BadLevel
  use vect_Utils
  use sidl_PostViolation
  use sidl_PreViolation
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuProduct.use)
  use vect_BadLevel
  use sidl_double_array
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuProduct.use)
  implicit none
  real (kind=sidl_double) :: a
  ! in
  type(sidl__array) :: u
  ! in
  integer (kind=sidl_enum) :: badLevel
  ! in
  type(sidl__array) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuProduct)
    integer (kind=sidl_int) :: i, lenU, lowU
    real (kind=sidl_double) :: val
    type(sidl_double_1d)    :: du
    type(sidl_double_1d)    :: dretval
    call cast(u, du)

    call getInfo(u, lowU, lenU)
    if (badLevel .eq. NoVio) then
       if (lenU .gt. 0_sidl_int) then
          call createArray(lenU, retval)
          call cast(retval, dretval)
          if (not_null(retval)) then
             do i = 0_sidl_int, lenU - 1_sidl_int
                call get(du, lowU+i, val)
                call set(dretval, i, a * val)
             enddo
          else
             call set_null(retval)
          endif
       else
          call set_null(retval)
       endif
    else if (badLevel .eq. NullRes) then
       call set_null(retval)
    else if (badLevel .eq. TwoDRes) then
       call createMatrix(lenU, retval)
    else if (badLevel .eq. WrongSizeRes) then
       call createArray(lenU+5_sidl_int, retval)
    else
       call set_null(retval)
    endif

    return
! DO-NOT-DELETE splicer.end(vect.Utils.vuProduct)
end subroutine vect_Utils_vuProduct_mi


! 
! Method:  vuNegate[]
! Return the negation of the specified vector.
! 

recursive subroutine vect_Utils_vuNegate_mi(u, badLevel, retval, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_BadLevel
  use vect_Utils
  use sidl_PostViolation
  use sidl_PreViolation
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuNegate.use)
  use sidl_SIDLException
  use vect_BadLevel
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuNegate.use)
  implicit none
  type(sidl__array) :: u
  ! in
  integer (kind=sidl_enum) :: badLevel
  ! in
  type(sidl__array) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuNegate)
  integer (kind=sidl_int)    :: i, lenU, lowU
  type(sidl_SIDLException_t) :: sExcept
  type(sidl_BaseInterface_t) :: throwaway_exception
  real (kind=sidl_double)    :: a
  character (len=20)         :: myfilename
  character (len=22)         :: myname

  myfilename = 'vect_Utils_Impl.f'
  myname     = 'vect_Utils_vuNegate'

  a = -1.0 * 1.0_sidl_double
  call getInfo(u, lowU, lenU)
  if (badLevel .eq. NoVio) then
     if (lenU .gt. 0_sidl_int) then
        call vect_Utils_vuProduct_mi(a, u, NoVio, retval, exception)
        if (not_null(exception)) then
           call set_null(retval)
           call cast(exception, sExcept, throwaway_exception)
           if (not_null(sExcept)) then
              call add(sExcept, myfilename, 902_sidl_int, myname, &
                       throwaway_exception)
              call deleteRef(sExcept, throwaway_exception)
              return
           endif
        endif
     else
        call set_null(retval)
     endif
  else if (badLevel .eq. NullRes) then
     call set_null(retval)
  else if (badLevel .eq. TwoDRes) then
     call createMatrix(lenU, retval)
  else if (badLevel .eq. WrongSizeRes) then
     call createArray(lenU+5_sidl_int, retval)
  else
     call set_null(retval)
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuNegate)
end subroutine vect_Utils_vuNegate_mi


! 
! Method:  vuNormalize[]
! Return the normalizaton of the specified vector.
! 
! Note the tolerance is included because the implementation invokes 
! vuDot().
! 

recursive subroutine vect_Utils_vuNormalize_mi(u, tol, badLevel, retval,       &
  exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_BadLevel
  use vect_Utils
  use sidl_PostViolation
  use sidl_PreViolation
  use vect_vDivByZeroExcept
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuNormalize.use)
  use sidl_SIDLException
  use vect_BadLevel
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuNormalize.use)
  implicit none
  type(sidl__array) :: u
  ! in
  real (kind=sidl_double) :: tol
  ! in
  integer (kind=sidl_enum) :: badLevel
  ! in
  type(sidl__array) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuNormalize)
  integer (kind=sidl_int)         :: i, lenU, lowU
  type(sidl_SIDLException_t)      :: sExcept
  type(vect_vDivByZeroExcept_t) :: dbzExcept
  type(sidl_BaseInterface_t)      :: throwaway_exception
  real (kind=sidl_double)         :: valNorm
  character (len=20)              :: myfilename
  character (len=24)              :: myname
  character (len=80)              :: msg

  myfilename = 'vect_Utils_Impl.f'
  myname     = 'vect_Utils_vuNormalize'
  msg        = 'vuNormalize: vDivByZeroExcept: Cannot divide by zero.'

  call getInfo(u, lowU, lenU)
  if (badLevel .eq. NoVio) then
     if (lenU .gt. 0_sidl_int) then
        call vect_Utils_vuNorm_mi(u, tol, NoVio, valNorm, exception)
        if (is_null(exception)) then
           if (valNorm .ne. 0.0_sidl_double) then
              call vect_Utils_vuProduct_mi(1.0_sidl_double/valNorm, &
                                             u, NoVio, retval, &
                                             exception)
              if (not_null(exception)) then
                 call set_null(retval)
                 call cast(exception, sExcept, throwaway_exception)
                 if (not_null(sExcept)) then
                    call add(sExcept, myfilename, 989_sidl_int, &
                             myname, throwaway_exception)
                    call deleteRef(sExcept, throwaway_exception)
                    return
                 endif
              endif
           else
              call set_null(retval)
              call new(dbzExcept, throwaway_exception)
              if (not_null(dbzExcept)) then
                 call setNote(dbzExcept, msg, throwaway_exception)
                 call add(dbzExcept, myfilename, 986_sidl_int, &
                          myname, throwaway_exception)
                 call cast(dbzExcept, exception, throwaway_exception)
                 call deleteRef(dbzExcept, throwaway_exception)
                 return
              endif
           endif
        else
           call set_null(retval)
           call cast(exception, sExcept, throwaway_exception)
           if (not_null(sExcept)) then
              call add(sExcept, myfilename, 986_sidl_int, myname, &
                       throwaway_exception)
              call deleteRef(sExcept, throwaway_exception)
           endif
        endif
     else
        call set_null(retval)
     endif
  else if (badLevel .eq. NullRes) then
     call set_null(retval)
  else if (badLevel .eq. TwoDRes) then
     call createMatrix(lenU, retval)
  else if (badLevel .eq. WrongSizeRes) then
     call createArray(lenU+5_sidl_int, retval)
  else
     call set_null(retval)
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuNormalize)
end subroutine vect_Utils_vuNormalize_mi


! 
! Method:  vuSum[]
! Return the sum of the specified vectors.
! 

recursive subroutine vect_Utils_vuSum_mi(u, v, badLevel, retval, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_BadLevel
  use vect_Utils
  use sidl_PostViolation
  use sidl_PreViolation
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuSum.use)
  use vect_BadLevel
  use sidl_double_array
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuSum.use)
  implicit none
  type(sidl__array) :: u
  ! in
  type(sidl__array) :: v
  ! in
  integer (kind=sidl_enum) :: badLevel
  ! in
  type(sidl__array) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuSum)
  integer (kind=sidl_int) :: i, lenU, lenV, lowU, lowV
  real (kind=sidl_double) :: ui, vi
  type(sidl_double_1d)    :: du
  type(sidl_double_1d)    :: dv
  type(sidl_double_1d)    :: dretval
  call cast(u, du)
  call cast(v, dv)

  call getInfo(u, lowU, lenU)
  if (badLevel .eq. NoVio) then
     call getInfo(v, lowV, lenV)
     if ( (lenU .gt. 0_sidl_int) .and. (lenU .eq. lenV) ) then
        call createArray(lenU, retVal)
        call cast(retval, dretval)
        if (not_null(retval)) then
           do i = 0_sidl_int, lenU - 1_sidl_int
              call get(du, lowU+i, ui)
              call get(dv, lowV+i, vi)
              call set(dretval, i, ui + vi)
           enddo
        endif
     else
        call set_null(retval)
     endif
  else if (badLevel .eq. NullRes) then
     call set_null(retval)
  else if (badLevel .eq. TwoDRes) then
     call createMatrix(lenU, retval)
  else if (badLevel .eq. WrongSizeRes) then
     call createArray(lenU+5_sidl_int, retval)
  else
     call set_null(retval)
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuSum)
end subroutine vect_Utils_vuSum_mi


! 
! Method:  vuDiff[]
! Return the difference of the specified vectors.
! 

recursive subroutine vect_Utils_vuDiff_mi(u, v, badLevel, retval, exception)
  use sidl
  use sidl_BaseInterface
  use sidl_RuntimeException
  use vect_BadLevel
  use vect_Utils
  use sidl_PostViolation
  use sidl_PreViolation
  use sidl_array_array
  use vect_Utils_impl
  ! DO-NOT-DELETE splicer.begin(vect.Utils.vuDiff.use)
  use vect_BadLevel
  use sidl_double_array
  ! DO-NOT-DELETE splicer.end(vect.Utils.vuDiff.use)
  implicit none
  type(sidl__array) :: u
  ! in
  type(sidl__array) :: v
  ! in
  integer (kind=sidl_enum) :: badLevel
  ! in
  type(sidl__array) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out

! DO-NOT-DELETE splicer.begin(vect.Utils.vuDiff)
  integer (kind=sidl_int) :: i, lenU, lenV, lowU, lowV
  real (kind=sidl_double) :: ui, vi
  type(sidl_double_1d)    :: du
  type(sidl_double_1d)    :: dv
  type(sidl_double_1d)    :: dretval
  call cast(u, du)
  call cast(v, dv)

  call getInfo(u, lowU, lenU)
  if (badLevel .eq. NoVio) then
     call getInfo(v, lowV, lenV)
     if ( (lenU .gt. 0_sidl_int) .and. (lenU .eq. lenV) ) then
        call createArray(lenU, retval)
        call cast(retval, dretval)
        if (not_null(retval)) then
           do i = 0_sidl_int, lenU - 1_sidl_int
              call get(du, lowU+i, ui)
              call get(dv, lowV+i, vi)
              call set(dretval, i, ui - vi)
           enddo
        endif
     else
        call set_null(retval)
     endif
  else if (badLevel .eq. NullRes) then
     call set_null(retval)
  else if (badLevel .eq. TwoDRes) then
     call createMatrix(lenU, retval)
  else if (badLevel .eq. WrongSizeRes) then
     call createArray(lenU+5_sidl_int, retval)
  else
     call set_null(retval)
  endif

  return
! DO-NOT-DELETE splicer.end(vect.Utils.vuDiff)
end subroutine vect_Utils_vuDiff_mi


! DO-NOT-DELETE splicer.begin(_miscellaneous_code_end)
! insert code here (extra code)
! DO-NOT-DELETE splicer.end(_miscellaneous_code_end)
