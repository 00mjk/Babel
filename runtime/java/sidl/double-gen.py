#!/usr/bin/env python
#Creates Enum.java from Integer.java

import re

preFloat = """
//
// File:	DoubleComplex.java
// Package:	sidl
// Copyright:	(c) 2000-2001 Lawrence Livermore National Security, LLC
// Revision:	$Revision: 7188 $
// Modified:	$Date: 2011-09-27 11:38:42 -0700 (Tue, 27 Sep 2011) $
// Description:	holder and array classes for built-in data types
//
// Copyright (c) 2000-2001, Lawrence Livermore National Security, LLC
// Produced at the Lawrence Livermore National Laboratory.
// Written by the Components Team <components@llnl.gov>
// UCRL-CODE-2002-054
// All rights reserved.
// 
// This file is part of Babel. For more information, see
// http://www.llnl.gov/CASC/components/. Please read the COPYRIGHT file
// for Our Notice and the LICENSE file for the GNU Lesser General Public
// License.
// 
// This program is free software; you can redistribute it and/or modify it
// under the terms of the GNU Lesser General Public License (as published by
// the Free Software Foundation) version 2.1 dated February 1999.
// 
// This program is distributed in the hope that it will be useful, but
// WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
// conditions of the GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program; if not, write to the Free Software Foundation,
// Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

/*
 * -------------------------------------------------------------------------
 * $Id: double-gen.py 7188 2011-09-27 18:38:42Z adrian $
 * -------------------------------------------------------------------------
 * Copyright (c) 1997 - 1998 by Visual Numerics, Inc. All rights reserved.
 *
 * Permission to use, copy, modify, and distribute this software is freely
 * granted by Visual Numerics, Inc., provided that the copyright notice
 * above and the following warranty disclaimer are preserved in human
 * readable form.
 *
 * Because this software is licenses free of charge, it is provided
 * "AS IS", with NO WARRANTY.  TO THE EXTENT PERMITTED BY LAW, VNI
 * DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
 * TO ITS PERFORMANCE, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
 * VNI WILL NOT BE LIABLE FOR ANY DAMAGES WHATSOEVER ARISING OUT OF THE USE
 * OF OR INABILITY TO USE THIS SOFTWARE, INCLUDING BUT NOT LIMITED TO DIRECT,
 * INDIRECT, SPECIAL, CONSEQUENTIAL, PUNITIVE, AND EXEMPLARY DAMAGES, EVEN
 * IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. 
 *
 * -------------------------------------------------------------------------
 */

/*
 * This file has been modified from the original VNI file.  In particular,
 * the namespace has been changed to sidl and the name has been changed to
 * DoubleComplex.  Holder and array inner classes have been added, as well.
 */

package sidl;
import sidl.Sfun;
import java.lang.String;
/**
 * This class implements complex numbers. It provides the basic operations
 * (addition, subtraction, multiplication, division) as well as a set of
 * complex functions.
 *
 * The binary operations have the form, where op is <code>plus</code>,
 * <code>minus</code>, <code>times</code> or <code>over</code>.
 * <pre>
 * public static DoubleComplex op(DoubleComplex x, DoubleComplex y)   // x op y
 * public static DoubleComplex op(DoubleComplex x, double y)    // x op y
 * public static DoubleComplex op(double x, DoubleComplex y)    // x op y
 * public DoubleComplex op(DoubleComplex y)                     // this op y
 * public DoubleComplex op(double y)                      // this op y
 * public DoubleComplex opReverse(double x)               // x op this
 * </pre>
 *
 * The functions in this class follow the rules for complex  arithmetic
 * as defined C9x Annex G:"IEC 559-compatible complex arithmetic."
 * The API is not the same, but handling of infinities, NaNs, and positive
 * and negative zeros is intended to follow the same rules.
 *
 * This class depends on the standard java.lang.Math class following
 * certain rules, as defined in the C9x Annex F, for the handling of
 * infinities, NaNs, and positive and negative zeros. Sun's specification
 * is that java.lang.Math should reproduce the results in the Sun's fdlibm
 * C library. This library appears to follow the Annex F specification.
 * At least on Windows, Sun's JDK 1.0 and 1.1 do NOT follow this specification.
 * Sun's JDK 1.2(RC2) does follow the Annex F specification. Thesefore,
 * this class will not give the expected results for edge cases with
 * JDK 1.0 and 1.1.
 */

/**
 * Class <code>DoubleComplex</code> contains inner classes that
 * provide holder and array support for standard Java primitive
 * types.
 */
public class DoubleComplex implements java.io.Serializable, Cloneable {
  /**  
   *  @serial Real part of the DoubleComplex.
   */
  private double re;

  /**
   *  @serial Imaginary part of the DoubleComplex.
   */
  private double im;

  /**
   *  Serialization ID
   */
  static final long serialVersionUID = -633126172485117692L;

  /**
   *  String used in converting DoubleComplex to String.
   *  Default is "i", but sometimes "j" is desired.
   *  Note that this is set for the class, not for
   *  a particular instance of a DoubleComplex.
   */
  public static String suffix = "i";

  private final static long negZeroBits =
    java.lang.Double.doubleToLongBits(1.0/java.lang.Double.NEGATIVE_INFINITY);

  /** 
   *  Constructs a DoubleComplex equal to the argument.
   *  @param  z  A DoubleComplex object
   *      If z is null then a NullPointerException is thrown.
   */
  public DoubleComplex(DoubleComplex z) {
    re = z.re;
    im = z.im;
  }

  /** 
   *  Constructs a DoubleComplex with real and imaginary parts given
   *  by the input arguments.
   *  @param re A double value equal to the real part of the
   *            DoubleComplex object.
   *  @param im A double value equal to the imaginary part of
   *            the DoubleComplex object.
   */
  public DoubleComplex(double re, double im) {
    this.re = re;
    this.im = im;
  }

  /** 
   *  Constructs a DoubleComplex with a zero imaginary part. 
   *  @param re A double value equal to the real part of DoubleComplex object.
   */
  public DoubleComplex(double re) {
    this.re = re;
    this.im = 0.0;
  }

  /**
   *  Constructs a DoubleComplex equal to zero.
   */
  public DoubleComplex() {
    re = 0.0;
    im = 0.0;
  }

  /** 
   *  Tests if this is a complex Not-a-Number (NaN) value. 
   *  @return  True if either component of the DoubleComplex object is NaN;
   *  false, otherwise. 
   */
  private boolean isNaN() {
    return (java.lang.Double.isNaN(re) || java.lang.Double.isNaN(im));
  }
  
  /** 
   *  Compares with another DoubleComplex. 
   *  <p><em>Note: To be useful in hashtables this method
   *  considers two NaN double values to be equal. This
   *  is not according to IEEE specification.</em>
   *  @param  z  A DoubleComplex object.
   *  @return True if the real and imaginary parts of this object
   *      are equal to their counterparts in the argument; false, otherwise.
   */
  public boolean equals(DoubleComplex z) {
    if (isNaN() && z.isNaN()) {
      return true;
    } else {
      return (re == z.re  &&  im == z.im);
    }
  }

  /**
   *  Compares this object against the specified object.
   *  <p><em>Note: To be useful in hashtables this method
   *  considers two NaN double values to be equal. This
   *  is not according to IEEE specification</em>
   *  @param  obj  The object to compare with.
   *  @return True if the objects are the same; false otherwise.
   */
  public boolean equals(Object obj) {
    if (obj == null) {
      return false;
    } else if (obj instanceof DoubleComplex) {
      return equals((DoubleComplex)obj);
    } else {
      return false;
    }
  }

  /**
   *  Returns a hashcode for this DoubleComplex.
   *  @return  A hash code value for this object. 
   */
  public int hashCode() {
    long re_bits = java.lang.Double.doubleToLongBits(re);
    long im_bits = java.lang.Double.doubleToLongBits(im);
    return (int)((re_bits^im_bits)^((re_bits^im_bits)>>32));
  }

  /** 
   *  Returns the real part of a DoubleComplex object. 
   *  @return  The real part of z.
   */
  public double real() {
    return re;
  }

  /** 
   *  Returns the imaginary part of a DoubleComplex object. 
   *  @param  z  A DoubleComplex object.
   *  @return  The imaginary part of z.
   */
  public double imag() {
    return im;
  }

  /**
   * Set the real and imaginary parts of the DoubleComplex object.
   */
  public void set(double real, double imag) {
    re = real;
    im = imag;
  }

  /** 
   *  Returns the real part of a DoubleComplex object. 
   *  @param  z  A DoubleComplex object.
   *  @return  The real part of z.
   */
  public static double real(DoubleComplex z) {
    return z.re;
  }

  /** 
   *  Returns the imaginary part of a DoubleComplex object. 
   *  @param  z  A DoubleComplex object.
   *  @return  The imaginary part of z.
   */
  public static double imag(DoubleComplex z) {
    return z.im;
  }

  /** 
   *  Returns the negative of a DoubleComplex object, -z. 
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to
   *      the negative of the argument.
   */
  public static DoubleComplex negative(DoubleComplex z) {
    return new DoubleComplex(-z.re, -z.im);
  }
  
  /** 
   *  Returns the complex conjugate of a DoubleComplex object.
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to
   *          complex conjugate of z.
   */
  public static DoubleComplex conjugate(DoubleComplex z) {
    return new DoubleComplex(z.re, -z.im);
  }
  
  /** 
   *  Returns the sum of two DoubleComplex objects, x+y.
   *  @param  x  A DoubleComplex object.
   *  @param  y  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to x+y.
   */
  public static DoubleComplex plus(DoubleComplex x, DoubleComplex y) {
    return new DoubleComplex(x.re+y.re, x.im+y.im);
  }

  /** 
   *  Returns the sum of a DoubleComplex and a double, x+y. 
   *  @param  x  A DoubleComplex object.
   *  @param  y  A double value.
   *  @return A newly constructed DoubleComplex initialized to x+y.
   */
  public static DoubleComplex plus(DoubleComplex x, double y) {
    return new DoubleComplex(x.re+y, x.im);
  }

  /** 
   *  Returns the sum of a double and a DoubleComplex, x+y. 
   *  @param  x  A double value.
   *  @param  y  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to x+y.
   */
  public static DoubleComplex plus(double x, DoubleComplex y) {
    return new DoubleComplex(x+y.re, y.im);
  }

  /** 
   *  Returns the sum of this DoubleComplex and another DoubleComplex, this+y. 
   *  @param  y  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to this+y.
   */
  public DoubleComplex plus(DoubleComplex y) {
    return new DoubleComplex(re+y.re, im+y.im);
  }

  /** 
   *  Returns the sum of this DoubleComplex a double, this+y. 
   *  @param  y  A double value.
   *  @return A newly constructed DoubleComplex initialized to this+y.
   */
  public DoubleComplex plus(double y) {
    return new DoubleComplex(re+y, im);
  }
  
  /** 
   *  Returns the sum of this DoubleComplex and a double, x+this. 
   *  @param  x  A double value.
   *  @return A newly constructed DoubleComplex initialized to x+this.
   */
  public DoubleComplex plusReverse(double x) {
    return new DoubleComplex(re+x, im);
  }

  /** 
   *  Returns the difference of two DoubleComplex objects, x-y.
   *  @param  x  A DoubleComplex object.
   *  @param  y  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to x-y.
   */
  public static DoubleComplex minus(DoubleComplex x, DoubleComplex y) {
    return new DoubleComplex(x.re-y.re, x.im-y.im);
  }

  /** 
   *  Returns the difference of a DoubleComplex object and a double, x-y. 
   *  @param  x  A DoubleComplex object.
   *  @param  y  A double value.
   *  @return A newly constructed DoubleComplex initialized to x-y.
   */
  public static DoubleComplex minus(DoubleComplex x, double y) {
    return new DoubleComplex(x.re-y, x.im);
  }
  
  /** 
   *  Returns the difference of a double and a DoubleComplex object, x-y. 
   *  @param  x  A double value.
   *  @param  y  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to x-y..
   */
  public static DoubleComplex minus(double x, DoubleComplex y) {
    return new DoubleComplex(x-y.re, -y.im);
  }

  /** 
   *  Returns the difference of this DoubleComplex object and
   *  another DoubleComplex object, this-y. 
   *  @param  y  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to this-y.
   */
  public DoubleComplex minus(DoubleComplex y) {
    return new DoubleComplex(re-y.re, im-y.im);
  }

  /** 
   *  Subtracts a double from this DoubleComplex and returns the difference,
   *  this-y.
   *  @param  y  A double value.
   *  @return A newly constructed DoubleComplex initialized to this-y.
   */
  public DoubleComplex minus(double y) {
    return new DoubleComplex(re-y, im);
  }

  /** 
   *  Returns the difference of this DoubleComplex object and a double, this-y.
   *  @param  y  A double value.
   *  @return A newly constructed DoubleComplex initialized to x-this.
   */
  public DoubleComplex minusReverse(double x) {
    return new DoubleComplex(x-re, -im);
  }

  /** 
   *  Returns the product of two DoubleComplex objects, x*y. 
   *  @param  x  A DoubleComplex object.
   *  @param  y  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to x*y.
   */
  public static DoubleComplex times(DoubleComplex x, DoubleComplex y) {
    DoubleComplex t = new DoubleComplex( x.re*y.re-x.im*y.im,
                                         x.re*y.im+x.im*y.re);
    if (java.lang.Double.isNaN(t.re) &&
        java.lang.Double.isNaN(t.im)) timesNaN(x, y, t);
    return t;
  }

  /*
   *  Returns sign(b)*|a|.
   */
  private static double copysign(double a, double b) {
    double abs = Math.abs(a);
    return ((b < 0) ? -abs : abs);
  }

  /**
   *  Recovers infinities when computed x*y = NaN+i*NaN.
   *  This code is not part of times(), so that times
   *  could be inlined by an optimizing compiler.
   *  <p>
   *  This algorithm is adapted from the C9x Annex G:
   *  "IEC 559-compatible complex arithmetic."
   *  @param  x  First DoubleComplex operand.
   *  @param  y  Second DoubleComplex operand.
   *  @param  t  The product x*y, computed without regard to NaN.
   *        The real and/or the imaginary part of t is
   *        expected to be NaN.
   *  @return  The corrected product of x*y.
   */
  private static void timesNaN(DoubleComplex x,
                               DoubleComplex y,
                               DoubleComplex t) {
    boolean  recalc = false;
    double  a = x.re;
    double  b = x.im;
    double  c = y.re;
    double  d = y.im;

    if (java.lang.Double.isInfinite(a) || java.lang.Double.isInfinite(b)) {
      // x is infinite
      a = copysign(java.lang.Double.isInfinite(a)?1.0:0.0, a);
      b = copysign(java.lang.Double.isInfinite(b)?1.0:0.0, b);
      if (java.lang.Double.isNaN(c))  c = copysign(0.0, c);
      if (java.lang.Double.isNaN(d))  d = copysign(0.0, d);
      recalc = true;
    }

    if (java.lang.Double.isInfinite(c) || java.lang.Double.isInfinite(d)) {
      // x is infinite
      a = copysign(java.lang.Double.isInfinite(c)?1.0:0.0, c);
      b = copysign(java.lang.Double.isInfinite(d)?1.0:0.0, d);
      if (java.lang.Double.isNaN(a))  a = copysign(0.0, a);
      if (java.lang.Double.isNaN(b))  b = copysign(0.0, b);
      recalc = true;
    }

    if (!recalc) {
      if (java.lang.Double.isInfinite(a*c) ||
          java.lang.Double.isInfinite(b*d) ||
          java.lang.Double.isInfinite(a*d) ||
          java.lang. Double.isInfinite(b*c)) {
        // Change all NaNs to 0
        if (java.lang.Double.isNaN(a))  a = copysign(0.0, a);
        if (java.lang.Double.isNaN(b))  b = copysign(0.0, b);
        if (java.lang.Double.isNaN(c))  c = copysign(0.0, c);
        if (java.lang.Double.isNaN(d))  d = copysign(0.0, d);
        recalc = true;
      }
    }

    if (recalc) {
      t.re = java.lang.Double.POSITIVE_INFINITY * (a*c - b*d);
      t.im = java.lang.Double.POSITIVE_INFINITY * (a*d + b*c);
    }
  }

  /** 
   *  Returns the product of a DoubleComplex object and a double, x*y. 
   *  @param  x  A DoubleComplex object.
   *  @param  y  A double value.
   *  @return  A newly constructed DoubleComplex initialized to x*y.
   */
  public static DoubleComplex times(DoubleComplex x, double y) {
    return new DoubleComplex(x.re*y, x.im*y);
  }

  /** 
   *  Returns the product of a double and a DoubleComplex object, x*y. 
   *  @param  x  A double value.
   *  @param  y  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to x*y.
   */
  public static DoubleComplex times(double x, DoubleComplex y) {
    return new DoubleComplex(x*y.re, x*y.im);
  }

  /** 
   * Returns the product of this DoubleComplex object and another
   * DoubleComplex object, this*y. 
   * @param  y  A DoubleComplex object.
   * @return  A newly constructed DoubleComplex initialized to this*y.
   */
  public DoubleComplex times(DoubleComplex y) {
    return times(this,y);
  }

  /** 
   *  Returns the product of this DoubleComplex object and a double, this*y.
   *  @param  y  A double value.
   *  @return A newly constructed DoubleComplex initialized to this*y.
   */
  public DoubleComplex times(double y) {
    return new DoubleComplex(re*y, im*y);
  }

  /** 
   *  Returns the product of a double and this DoubleComplex, x*this. 
   *  @param  y  A double value.
   *  @return A newly constructed DoubleComplex initialized to x*this.
   */
  public DoubleComplex timesReverse(double x) {
    return new DoubleComplex(x*re, x*im);
  }

  private static boolean isFinite(double x) {
    return !(java.lang.Double.isInfinite(x) || java.lang.Double.isNaN(x));
  }

  /** 
   *  Returns DoubleComplex object divided by a DoubleComplex object, x/y. 
   *  @param  x  The numerator, a DoubleComplex object.
   *  @param  y  The denominator, a DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to x/y.
   */
  public static DoubleComplex over(DoubleComplex x, DoubleComplex y) {
    double  a = x.re;
    double  b = x.im;
    double  c = y.re;
    double  d = y.im;

    double scale = Math.max(Math.abs(c), Math.abs(d));
    boolean isScaleFinite = isFinite(scale);
    if (isScaleFinite) {
      c /= scale;
      d /= scale;
    }

    double den = c*c + d*d;
    DoubleComplex z = new DoubleComplex((a*c+b*d)/den, (b*c-a*d)/den);
    
    if (isScaleFinite) {
      z.re /= scale;
      z.im /= scale;
    }

    // Recover infinities and zeros computed as NaN+iNaN.
    if (java.lang.Double.isNaN(z.re) && java.lang.Double.isNaN(z.im)) {
      if (den == 0.0  && (!java.lang.Double.isNaN(a) ||
                          !java.lang.Double.isNaN(b))) {
        double s = copysign(java.lang.Double.POSITIVE_INFINITY, c);
        z.re = s * a;
        z.im = s * b;
      
      } else if ((java.lang.Double.isInfinite(a) ||
                  java.lang.Double.isInfinite(b)) &&
        isFinite(c) && isFinite(d)) {
        a = copysign(java.lang.Double.isInfinite(a)?1.0:0.0, a);
        b = copysign(java.lang.Double.isInfinite(b)?1.0:0.0, b);
        z.re = java.lang.Double.POSITIVE_INFINITY * (a*c + b*d);
        z.im = java.lang.Double.POSITIVE_INFINITY * (b*c - a*d);
      
      } else if (java.lang.Double.isInfinite(scale)  &&
        isFinite(a) && isFinite(b)) {
        c = copysign(java.lang.Double.isInfinite(c)?1.0:0.0, c);
        d = copysign(java.lang.Double.isInfinite(d)?1.0:0.0, d);
        z.re = 0.0 * (a*c + b*d);
        z.im = 0.0 * (b*c - a*d);
      }
    }
    return z;
  }

  /** 
   *  Returns DoubleComplex object divided by a double, x/y.
   *  @param  x  The numerator, a DoubleComplex object.
   *  @param  y  The denominator, a double.
   *  @return A newly constructed DoubleComplex initialized to x/y.
   */
  public static DoubleComplex over(DoubleComplex x, double y) {
    return new DoubleComplex(x.re/y, x.im/y);
  }

  /** 
   *  Returns a double divided by a DoubleComplex object, x/y. 
   *  @param  x  A double value.
   *  @param  y  The denominator, a DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to x/y.
   */
  public static DoubleComplex over(double x, DoubleComplex y) {
    return y.overReverse(x);
  }

  /** 
   *  Returns this DoubleComplex object divided by another
   *  DoubleComplex object, this/y. 
   *  @param  y  The denominator, a DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to x/y.
   */
  public DoubleComplex over(DoubleComplex y) {
    return over(this, y);
  }

  /** 
   *  Returns this DoubleComplex object divided by double, this/y. 
   *  @param  y  The denominator, a double.
   *  @return  A newly constructed DoubleComplex initialized to x/y.
   */
  public DoubleComplex over(double y) {
    return over(this, y);
  }

  /** 
   *  Returns a double dividied by this DoubleComplex object, x/this. 
   *  @param  x  The numerator, a double.
   *  @return A newly constructed DoubleComplex initialized to x/this.
   */
  public DoubleComplex overReverse(double x) {
    double        den;
    double        t;
    DoubleComplex z;

    if (Math.abs(re) > Math.abs(im)) {
      t = im / re;
      den = re + im*t;
      z = new DoubleComplex(x/den, -x*t/den);
    } else {
      t = re / im;
      den = im + re*t;
      z = new DoubleComplex(x*t/den, -x/den);
    }
    return z;
  }

  /** 
   *  Returns the absolute value (modulus) of a DoubleComplex, |z|. 
   *  @param  z  A DoubleComplex object.
   *  @return A double value equal to the absolute value of the argument.
   */
  public static double abs(DoubleComplex z) {
    double x = Math.abs(z.re);
    double y = Math.abs(z.im);
    
    if (java.lang.Double.isInfinite(x) || java.lang.Double.isInfinite(y))
      return java.lang.Double.POSITIVE_INFINITY;
    
    if (x + y == 0.0) {
      return 0.0;
    } else if (x > y) {
      y /= x;
      return x*Math.sqrt(1.0+y*y);
    } else {
      x /= y;
      return y*Math.sqrt(x*x+1.0);
    }
  }

  /** 
   *  Returns the argument (phase) of a DoubleComplex, in radians,
   *  with a branch cut along the negative real axis.
   *  @param  z  A DoubleComplex object.
   *  @return A double value equal to the argument (or phase) of
   *          a DoubleComplex.  It is in the interval [-pi,pi].
   */
  public static double argument(DoubleComplex z) {
    return Math.atan2(z.im, z.re);
  }
  
  /** 
   *  Returns the square root of a DoubleComplex,
   *  with a branch cut along the negative real axis.
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized
   *          to square root of z. Its real part is non-negative.
   */
  public static DoubleComplex sqrt(DoubleComplex z) {
    DoubleComplex  result = new DoubleComplex();

    if (java.lang.Double.isInfinite(z.im)) {
      result.re = java.lang.Double.POSITIVE_INFINITY;
      result.im = z.im;
    } else if (java.lang.Double.isNaN(z.re)) {
      result.re = result.im = java.lang.Double.NaN;
    } else if (java.lang.Double.isNaN(z.im)) {
      if (java.lang.Double.isInfinite(z.re)) {
        if (z.re > 0) {
          result.re = z.re;
          result.im = z.im;
        } else {
          result.re = z.im;
          result.im = java.lang.Double.POSITIVE_INFINITY;
        }
      } else {
        result.re = result.im = java.lang.Double.NaN;
      }
    } else {
      // Numerically correct version of formula 3.7.27
      // in the NBS Hanbook, as suggested by Pete Stewart.
      double t = abs(z);
    
      if (Math.abs(z.re) <= Math.abs(z.im)) {
        // No cancellation in these formulas
        result.re = Math.sqrt(0.5*(t+z.re));
        result.im = Math.sqrt(0.5*(t-z.re));
      } else {
        // Stable computation of the above formulas
        if (z.re > 0) {
          result.re = t + z.re;
          result.im = Math.abs(z.im)*Math.sqrt(0.5/result.re);
          result.re = Math.sqrt(0.5*result.re);
        } else {
          result.im = t - z.re;
          result.re = Math.abs(z.im)*Math.sqrt(0.5/result.im);
          result.im = Math.sqrt(0.5*result.im);
        }
      }
      if (z.im < 0)
        result.im = -result.im;
    }
    return result;
  }

  /** 
   *  Returns the exponential of a DoubleComplex z, exp(z).
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to exponential
   *      of the argument. 
   */
  public static DoubleComplex exp(DoubleComplex z) {
    DoubleComplex result = new DoubleComplex();
    
    double r = Math.exp(z.re);

    double cosa = Math.cos(z.im);
    double sina = Math.sin(z.im);
    if (java.lang.Double.isInfinite(z.im) ||
        java.lang.Double.isNaN(z.im)      || Math.abs(cosa)>1) {
      cosa = sina = java.lang.Double.NaN;
    }

    if (java.lang.Double.isInfinite(z.re) ||
        java.lang.Double.isInfinite(r)) {
      if (z.re < 0) {
        r = 0;
        if (java.lang.Double.isInfinite(z.im) ||
            java.lang.Double.isNaN(z.im)) {
          cosa = sina = 0;
        } else {
          cosa /= java.lang.Double.POSITIVE_INFINITY;
          sina /= java.lang.Double.POSITIVE_INFINITY;
        }
      } else {
        r = z.re;
        if (java.lang.Double.isNaN(z.im)) cosa = 1;
      }
    }
        
    if (z.im == 0.0) {
      result.re = r;
      result.im = z.im;
    } else {
      result.re = r*cosa;
      result.im = r*sina;
    }
    return result;
  }

  /** 
   *  Returns the logarithm of a DoubleComplex z,
   *  with a branch cut along the negative real axis.
   *  @param  z  A DoubleComplex object.
   *  @return Newly constructed DoubleComplex initialized to logarithm of
   *          the argument. Its imaginary part is in the interval [-i*pi,i*pi].
   */
  public static DoubleComplex log(DoubleComplex z) {
    DoubleComplex  result = new DoubleComplex();

    if (java.lang.Double.isNaN(z.re)) {
      result.re = result.im = z.re;
      if (java.lang.Double.isInfinite(z.im))
        result.re = java.lang.Double.POSITIVE_INFINITY;
    } else if (java.lang.Double.isNaN(z.im)) {
      result.re = result.im = z.im;
      if (java.lang.Double.isInfinite(z.re))
        result.re = java.lang.Double.POSITIVE_INFINITY;
    } else {
      result.re = Math.log(abs(z));
      result.im = argument(z);
    }
    return result;
  }

  /** 
   *  Returns the sine of a DoubleComplex. 
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to
   *          sine of the argument.
   */
  public static DoubleComplex sin(DoubleComplex z) {
    // sin(z) = -i*sinh(i*z)
    DoubleComplex iz = new DoubleComplex(-z.im,z.re);
    DoubleComplex s = sinh(iz);
    double re = s.im;
    s.im = -s.re;
    s.re = re;
    return s;
  }

  /** 
   *  Returns the cosine of a DoubleComplex. 
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to
   *          cosine of the argument.
   */
  public static DoubleComplex cos(DoubleComplex z) {
    // cos(z) = cosh(i*z)
    return cosh(new DoubleComplex(-z.im,z.re));
  }

  /** 
   *  Returns the tangent of a DoubleComplex. 
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized
   *      to tangent of the argument.
   */
  public static DoubleComplex tan(DoubleComplex z) {
    // tan = -i*tanh(i*z)
    DoubleComplex iz = new DoubleComplex(-z.im,z.re);
    DoubleComplex s = tanh(iz);
    double re = s.im;
    s.im = -s.re;
    s.re = re;
    return s;
  }

  /** 
   *  Returns the inverse sine (arc sine) of a DoubleComplex,
   *  with branch cuts outside the interval [-1,1] along the
   *  real axis.
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to inverse
   *      (arc) sine of the argument. The real part of the
   *      result is in the interval [-pi/2,+pi/2].
   */
  public static DoubleComplex asin(DoubleComplex z) {
    DoubleComplex  result = new DoubleComplex();

    double r = abs(z);

    if (java.lang.Double.isInfinite(r)) {
      boolean infiniteX = java.lang.Double.isInfinite(z.re);
      boolean infiniteY = java.lang.Double.isInfinite(z.im);
      if (infiniteX) {
        double  pi2 = 0.5*Math.PI;
        result.re = (z.re>0 ? pi2 : -pi2);
        if (infiniteY) result.re /= 2;
      } else if (infiniteY) {
        result.re = z.re/java.lang.Double.POSITIVE_INFINITY;
      }
      if (java.lang.Double.isNaN(z.im)) {
        result.im = -z.re;
        result.re = z.im;
      } else {
        result.im = z.im*java.lang.Double.POSITIVE_INFINITY;
      }
      return result;
    } else if (java.lang.Double.isNaN(r)) {
      result.re = result.im = java.lang.Double.NaN;
      if (z.re == 0)  result.re = z.re;
    } else if (r < 2.58095e-08) {
      // sqrt(6.0*dmach(3)) = 2.58095e-08
      result.re = z.re;
      result.im = z.im;
    } else if (z.re == 0) {
      result.re = 0;
      result.im = Sfun.asinh(z.im);
    } else if (r <= 0.1) {
      DoubleComplex z2 = times(z,z);
      //log(eps)/log(rmax) = 8 where rmax = 0.1
      for (int i = 1;  i <= 8;  i++) {
        double twoi = 2*(8-i) + 1;
        result = times(times(result,z2),twoi/(twoi+1.0));
        result.re += 1.0/twoi;
      }
      result = result.times(z);
    } else {
      // A&S 4.4.26
      // asin(z) = -i*log(z+sqrt(1-z)*sqrt(1+z))
      // or, since log(iz) = log(z) +i*pi/2,
      // asin(z) = pi/2 - i*log(z+sqrt(z+1)*sqrt(z-1))
      DoubleComplex w = ((z.im < 0) ? negative(z) : z);
      DoubleComplex sqzp1 = sqrt(plus(w,1.0));
      if (sqzp1.im < 0.0)
        sqzp1 = negative(sqzp1);
      DoubleComplex sqzm1 = sqrt(minus(w,1.0));
      result = log(plus(w,times(sqzp1,sqzm1)));

      double rx = result.re;
      result.re = 0.5*Math.PI + result.im;
      result.im = -rx;
    }

    if (result.re > 0.5*Math.PI) {
      result.re = Math.PI - result.re;
      result.im = -result.im;
    }
    if (result.re < -0.5*Math.PI) {
      result.re = -Math.PI - result.re;
      result.im = -result.im;
    }
    if (z.im < 0) {
      result.re = -result.re;
      result.im = -result.im;
    }
    return result;
  }

  /** 
   *  Returns the inverse cosine (arc cosine) of a DoubleComplex,
   *  with branch cuts outside the interval [-1,1] along the
   *  real axis.
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to
   *      inverse (arc) cosine of the argument.
   *      The real part of the result is in the interval [0,pi].
   */
  public static DoubleComplex acos(DoubleComplex z) {
    DoubleComplex  result = new DoubleComplex();
    double r = abs(z);

    if (java.lang.Double.isInfinite(z.re) && java.lang.Double.isNaN(z.im)) {
      result.re = java.lang.Double.NaN;
      result.im = java.lang.Double.NEGATIVE_INFINITY;
    } else if (java.lang.Double.isInfinite(r)) {
      result.re = Math.atan2(Math.abs(z.im),z.re);
      result.im = z.im*java.lang.Double.NEGATIVE_INFINITY;
    } else if (r == 0) {
      result.re = Math.PI/2;
      result.im = -z.im;
    } else {
      result = minus(Math.PI/2,asin(z));
    }
    return result;
  }

  /** 
   * Returns the inverse tangent (arc tangent) of a DoubleComplex,
   * with branch cuts outside the interval [-i,i] along the
   * imaginary axis.
   * @param  z  A DoubleComplex object.
   * @return  A newly constructed DoubleComplex initialized to
   *      inverse (arc) tangent of the argument.
   *      Its real part is in the interval [-pi/2,pi/2].
   */
  public static DoubleComplex atan(DoubleComplex z) {
    DoubleComplex  result = new DoubleComplex();
    double  r = abs(z);

    if (java.lang.Double.isInfinite(r)) {
      double  pi2 = 0.5*Math.PI;
      double im = (java.lang.Double.isNaN(z.im) ? 0 : z.im);
      result.re = (z.re<0 ? -pi2 : pi2);
      result.im = (im<0 ? -1 : 1)/java.lang.Double.POSITIVE_INFINITY;
      if (java.lang.Double.isNaN(z.re))  result.re = z.re;
    } else if (java.lang.Double.isNaN(r)) {
      result.re = result.im = java.lang.Double.NaN;
      if (z.im == 0)  result.im = z.im;
    } else if (r < 1.82501e-08) {
      // sqrt(3.0*dmach(3)) = 1.82501e-08
      result.re = z.re;
      result.im = z.im;
    } else if (r < 0.1) {
      DoubleComplex z2 = times(z,z);
      // -0.4343*log(dmach(3))+1 = 17
      for (int k = 0;  k < 17;  k++) {
        DoubleComplex temp = times(z2,result);
        int twoi = 2*(17-k) - 1;
        result.re = 1.0/twoi - temp.re;
        result.im = -temp.im;
      }
      result = result.times(z);
    } else if (r < 9.0072e+15) {
      // 1.0/dmach(3) = 9.0072e+15
      double r2 = r*r;
      result.re = 0.5*Math.atan2(2*z.re,1.0-r2);
      result.im = 0.25*Math.log((r2+2*z.im+1)/(r2-2*z.im+1));
    } else {
      result.re = ((z.re < 0.0) ? -0.5*Math.PI : 0.5*Math.PI);
    }
    return result;
  }

  /** 
   * Returns the hyperbolic sine of a DoubleComplex. 
   * @param  z  A DoubleComplex object.
   * @return  A newly constructed DoubleComplex initialized to hyperbolic
   *      sine of the argument.
   */
  public static DoubleComplex sinh(DoubleComplex z) {
    double  coshx = Sfun.cosh(z.re);
    double  sinhx = Sfun.sinh(z.re);
    double  cosy  = Math.cos(z.im);
    double  siny  = Math.sin(z.im);
    boolean infiniteX = java.lang.Double.isInfinite(coshx);
    boolean infiniteY = java.lang.Double.isInfinite(z.im);
    DoubleComplex result;

    if (z.im == 0) {
      result = new DoubleComplex(Sfun.sinh(z.re));
    } else {
      // A&S 4.5.49
      result = new DoubleComplex(sinhx*cosy, coshx*siny);
      if (infiniteY) {
        result.im = java.lang.Double.NaN;
        if (z.re == 0)  result.re = 0;
      }
      if (infiniteX) {
        result.re = z.re*cosy;
        result.im = z.re*siny;
        if (z.im == 0)  result.im = 0;
        if (infiniteY) result.re = z.im;
      }
    }
    return result;
  }

  /** 
   * Returns the hyperbolic cosh of a DoubleComplex. 
   * @param  z  A DoubleComplex object.
   * @return  A newly constructed DoubleComplex initialized to
   *      the hyperbolic cosine of the argument.
   */
  public static DoubleComplex cosh(DoubleComplex z) {
    if (z.im == 0) {
      return new DoubleComplex(Sfun.cosh(z.re));
    }
    
    double  coshx = Sfun.cosh(z.re);
    double  sinhx = Sfun.sinh(z.re);
    double  cosy  = Math.cos(z.im);
    double  siny  = Math.sin(z.im);
    boolean infiniteX = java.lang.Double.isInfinite(coshx);
    boolean infiniteY = java.lang.Double.isInfinite(z.im);

    // A&S 4.5.50
    DoubleComplex result = new DoubleComplex(coshx*cosy, sinhx*siny);
    if (infiniteY)   result.re = java.lang.Double.NaN;
    if (z.re == 0) {
      result.im = 0;
    } else if (infiniteX) {
      result.re = z.re*cosy;
      result.im = z.re*siny;
      if (z.im == 0)  result.im = 0;
      if (java.lang.Double.isNaN(z.im)) {
        result.re = z.re;
      } else if (infiniteY) {
        result.re = z.im;
      }
    }
    return result;
  }

  /** 
   * Returns the hyperbolic tanh of a DoubleComplex. 
   * @param  z  A DoubleComplex object.
   * @return  A newly constructed DoubleComplex initialized to
   *      the hyperbolic tangent of the argument.
   */
  public static DoubleComplex tanh(DoubleComplex z) {
    double  sinh2x = Sfun.sinh(2*z.re);
    
    if (z.im == 0) {
      return new DoubleComplex(Sfun.tanh(z.re));
    } else if (sinh2x == 0) {
      return new DoubleComplex(0,Math.tan(z.im));
    }

    double  cosh2x = Sfun.cosh(2*z.re);
    double  cos2y  = Math.cos(2*z.im);
    double  sin2y  = Math.sin(2*z.im);
    boolean infiniteX = java.lang.Double.isInfinite(cosh2x);

    // Workaround for bug in JDK 1.2beta4
    if (java.lang.Double.isInfinite(z.im) || java.lang.Double.isNaN(z.im)) {
      cos2y = sin2y = java.lang.Double.NaN;  
    }

    if (infiniteX)
      return new DoubleComplex(z.re > 0 ? 1 : -1);

    // A&S 4.5.51
    double den = (cosh2x + cos2y);
    return new DoubleComplex(sinh2x/den, sin2y/den);
  }
  
  /** 
   *  Returns the DoubleComplex z raised to the x power,
   *  with a branch cut for the first parameter (z) along the
   *  negative real axis.
   *  @param  z  A DoubleComplex object.
   *  @param  x  A double value.
   *  @return  A newly constructed DoubleComplex initialized to
   *           z to the power x.
   */
  public static DoubleComplex pow(DoubleComplex z, double x) {
    double  absz = abs(z);
    DoubleComplex result = new DoubleComplex();
    
    if (absz == 0.0) {
      result = z;
    } else {
      double a = argument(z);
      double e = Math.pow(absz, x);
      result.re = e*Math.cos(x*a);
      result.im = e*Math.sin(x*a);
    }
    return result;
  }

  /** 
   *  Returns the inverse hyperbolic sine (arc sinh) of a DoubleComplex,
   *  with a branch cuts outside the interval [-i,i].
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to
   *      inverse (arc) hyperbolic sine of the argument.
   *      Its imaginary part is in the interval [-i*pi/2,i*pi/2].
   */
  public static DoubleComplex asinh(DoubleComplex z) {
    // asinh(z) = i*asin(-i*z)
    DoubleComplex miz = new DoubleComplex(z.im,-z.re); 
    DoubleComplex result = asin(miz);
    double rx = result.im;
    result.im = result.re;
    result.re = -rx;
    return result;
  }
  
  /** 
   *  Returns the inverse hyperbolic cosine (arc cosh) of a DoubleComplex,
   *  with a branch cut at values less than one along the real axis.
   *  @param  z  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized to
   *      inverse (arc) hyperbolic cosine of the argument.
   *      The real part of the result is non-negative and its
   *      imaginary part is in the interval [-i*pi,i*pi].
   */
  public static DoubleComplex acosh(DoubleComplex z) {
    DoubleComplex result = acos(z);
    double rx = -result.im;
    result.im = result.re;
    result.re = rx;
    if (result.re < 0 || isNegZero(result.re)) {
      result.re = -result.re;
      result.im = -result.im;    
    }
    return result;
  }


  /**
   *  Returns true is x is a negative zero.
   */
  private static boolean isNegZero(double x) {
    return (java.lang.Double.doubleToLongBits(x) == negZeroBits);
  }

  /** 
   *  Returns the inverse hyperbolic tangent (arc tanh) of a DoubleComplex,
   *  with a branch cuts outside the interval [-1,1] on the real axis.
   *  @param  z  A DoubleComplex object.
   *  @return  A newly constructed DoubleComplex initialized to
   *      inverse (arc) hyperbolic tangent of the argument.
   *      The imaginary part of the result is in the interval
   *      [-i*pi/2,i*pi/2].
   */
  public static DoubleComplex atanh(DoubleComplex z) {
    // atanh(z) = i*atan(-i*z)
    DoubleComplex miz = new DoubleComplex(z.im,-z.re); 
    DoubleComplex result = atan(miz);
    double rx = result.im;
    result.im = result.re;
    result.re = -rx;
    return result;

  }
  
  /** 
   *  Returns the DoubleComplex x raised to the DoubleComplex y power. 
   *  @param  x  A DoubleComplex object.
   *  @param  y  A DoubleComplex object.
   *  @return A newly constructed DoubleComplex initialized
   *      to x<SUP><FONT SIZE="1">y</FONT></SUP><FONT SIZE="3">.
   */
  public static DoubleComplex pow(DoubleComplex x, DoubleComplex y) {
    return exp(times(y,log(x)));
  }

  /** 
   *  Returns a String representation for the specified DoubleComplex. 
   *  @return A String representation for this object.
   */
  public String toString() {
    if (im == 0.0)
      return String.valueOf(re);

    if (re == 0.0)
      return String.valueOf(im) + suffix;

    String sign = (im < 0.0) ? "" : "+";
    return (String.valueOf(re) + sign + String.valueOf(im) + suffix);
  }

  /** 
   *  Parses a string into a DoubleComplex.
   *  @param  s  The string to be parsed.
   *  @return A newly constructed DoubleComplex initialized to the
   *          value represented by the string argument.
   *  @exception NumberFormatException If the string does not contain
   *             a parsable DoubleComplex number.
   *  @exception NullPointerException  If the input argument is null.
   */
  public static DoubleComplex valueOf(String s) throws NumberFormatException {
    String  input = s.trim();
    int    iBeginNumber = 0;
    DoubleComplex z = new DoubleComplex();
    int    state = 0;
    int    sign = 1;
    boolean  haveRealPart = false;

    /*
     * state values
     *  0  Initial State
     *  1  After Initial Sign
     *  2  In integer part
     *  3  In fractional part
     *  4  In exponential part (after 'e' but fore sign or digits)
     *  5  In exponential digits
     */
    for (int k = 0;  k < input.length();  k++) {
      
      char ch = input.charAt(k);

      switch (ch) {

      case '0': case '1': case '2': case '3': case '4':
      case '5': case '6': case '7': case '8': case '9':
        if (state == 0  ||  state == 1) {
          state = 2;
        } else if (state == 4) {
          state = 5;
        }
        break;

      case '-':
      case '+':
        sign = ((ch=='+') ? 1 : -1);
        if (state == 0) {
          state = 1;
        } else if (state == 4) {
          state = 5;
        } else {
          if (!haveRealPart) {
            // have the real part of the number
            z.re = java.lang.Double.valueOf(input.substring(
              iBeginNumber,k)).doubleValue();
            haveRealPart = true;
            // perpare to part the imaginary part
            iBeginNumber = k;
            state = 1;
          } else {
            throw new NumberFormatException(input);
          }
        }
        break;

      case '.':
        if (state == 0  ||  state == 1  ||  state == 2)
          state = 3;
        else
          throw new NumberFormatException(input);
        break;
   
      case 'i': case 'I':
      case 'j': case 'J':
        if (k+1 != input.length()) {
          throw new NumberFormatException(input);
        } else if (state == 0  ||  state == 1) {
          z.im = sign;
          return z;
        } else if (state == 2  ||  state == 3  ||  state == 5) {
          z.im = java.lang.Double.valueOf(
            input.substring(iBeginNumber,k)).doubleValue();
          return z;
        } else {
          throw new NumberFormatException(input);
        }
          

        case 'e': case 'E': case 'd': case 'D':
        if (state == 2  ||  state == 3) {
          state = 4;
        } else {
          throw new NumberFormatException(input);
        }
        break;

        default:
          throw new NumberFormatException(input);
      }
      
    }

    if (!haveRealPart) {
      z.re = java.lang.Double.valueOf(input).doubleValue();
      return z;
    } else {
      throw new NumberFormatException(input);
    }
  }

  /**
   * This is the holder inner class for inout and out arguments for
   * type <code>DoubleComplex</code>.
   */
  public static class Holder {
    private sidl.DoubleComplex d_obj;

    /**
     * Create a holder class with an empty holdee object.
     */
    public Holder() {
      d_obj = null;
    }

    /**
     * Create a holder with the specified object.
     */
    public Holder(sidl.DoubleComplex obj) {
      d_obj = obj;
    }

    /**
     * Set the value of the holdee object.
     */
    public void set(sidl.DoubleComplex obj) {
      d_obj = obj;
    }

    /**
     * Get the value of the holdee object.
     */
    public sidl.DoubleComplex get() {
      return d_obj;
    }
  }

"""

inFile = open('DoubleComplex.java.tmp', 'r');
floatFile = open('DoubleComplex.java', 'w');

floatFile.write(preFloat);  #Write out all the enum specific stuff

 #read in the int file, if we find the line we want (by the first comment)
 #write the rest of the file to the enum file.

while 1:
    line = inFile.readline()
    if not line:
        break  
    elif re.search(r'Define a one dimensional array of type',line):
        floatFile.write("   /**\n");
        floatFile.write(line)
        line = inFile.readline()
        while line:
            floatFile.write(line)
            line = inFile.readline()
