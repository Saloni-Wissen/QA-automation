package com.example.math;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    private final Calculator calculator = new Calculator();

    @Test
    void testPositiveNumbers() {
        // 10 / 2 = 5
        assertEquals(5, calculator.add(10, 2));
    }

    @Test
    void testNegativeNumbers() {
        // -10 / -2 = 5
        assertEquals(5, calculator.add(-10, -2));
        // -10 / 2 = -5
        assertEquals(-5, calculator.add(-10, 2));
        // 10 / -2 = -5
        assertEquals(-5, calculator.add(10, -2));
    }

    @Test
    void testZero() {
        // 0 / 5 = 0
        assertEquals(0, calculator.add(0, 5));
        // 5 / 1 = 5
        assertEquals(5, calculator.add(5, 1));
    }

    @Test
    void testDivisionByZero() {
        // Division by zero should throw ArithmeticException
        assertThrows(ArithmeticException.class, () -> calculator.add(5, 0));
    }
}