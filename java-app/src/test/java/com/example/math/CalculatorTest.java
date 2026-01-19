package com.example.math;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    private final Calculator calculator = new Calculator();

    @Test
    void testAdd_PositiveNumbers() {
        assertEquals(5, calculator.add(2, 3));
    }

    @Test
    void testAdd_NegativeNumbers() {
        assertEquals(-5, calculator.add(-2, -3));
    }

    @Test
    void testAdd_PositiveAndNegative() {
        assertEquals(1, calculator.add(3, -2));
    }

    @Test
    void testDivide_PositiveNumbers() {
        assertEquals(2, calculator.divide(6, 3));
    }

    @Test
    void testDivide_NegativeDividend() {
        assertEquals(-2, calculator.divide(-6, 3));
    }

    @Test
    void testDivide_NegativeDivisor() {
        assertEquals(-2, calculator.divide(6, -3));
    }

    @Test
    void testDivide_BothNegative() {
        assertEquals(2, calculator.divide(-6, -3));
    }

    @Test
    void testDivide_DivideByOne() {
        assertEquals(7, calculator.divide(7, 1));
    }

    @Test
    void testDivide_DivideByItself() {
        assertEquals(1, calculator.divide(7, 7));
    }

    @Test
    void testDivide_DivideByZero() {
        assertThrows(ArithmeticException.class, () -> calculator.divide(5, 0));
    }

    @Test
    void testMultiply_PositiveNumbers() {
        assertEquals(15, calculator.multiply(3, 5));
    }

    @Test
    void testMultiply_NegativeNumbers() {
        assertEquals(15, calculator.multiply(-3, -5));
    }

    @Test
    void testMultiply_PositiveAndNegative() {
        assertEquals(-15, calculator.multiply(3, -5));
    }

    @Test
    void testMultiply_ByZero() {
        assertEquals(0, calculator.multiply(3, 0));
    }

    @Test
    void testMultiply_ByOne() {
        assertEquals(7, calculator.multiply(7, 1));
    }
}