package com.password_generator;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class AppTest {
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue() {
        assertTrue(true);
    }

    // Test to make sure the length is the passed in, requested length
    @Test
    public void test_length() {
        Password pw = new Password();
        pw.GeneratePassword(10);
        String password = pw.GetPassword();

        assertTrue(password.length() == 10);
    }

    // Test to ensure min length
    @Test
    public void test_min_length() {
        Password pw = new Password();
        pw.GeneratePassword(7);
        String password = pw.GetPassword();

        assertTrue(password.length() == 0);
    }

    // Test to ensure max length
    @Test
    public void test_max_length() {
        Password pw = new Password();
        pw.GeneratePassword(95);
        String password = pw.GetPassword();

        assertTrue(password.length() == 0);
    }

    // Use regex to test to ensure the password has a capital letter
    @Test
    public void test_has_capital() {
        Password pw = new Password();
        pw.GeneratePassword(10);
        String password = pw.GetPassword();

        assertTrue(password.matches(".*[A-Z].*"));
    }

    // Use regex to test to ensure the password has a lowercase letter
    @Test
    public void test_has_lowercase() {
        Password pw = new Password();
        pw.GeneratePassword(10);
        String password = pw.GetPassword();

        assertTrue(password.matches(".*[a-z].*"));
    }

    // Use regex to test to ensure the password has a number
    @Test
    public void test_has_number() {
        Password pw = new Password();
        pw.GeneratePassword(10);
        String password = pw.GetPassword();

        assertTrue(password.matches(".*\\d.*"));
    }

    // Use regex to test to ensure the password has a symbol / punctiation
    @Test
    public void test_has_symbol() {
        Password pw = new Password();
        pw.GeneratePassword(10);
        String password = pw.GetPassword();

        assertTrue(password.matches(".*[!\"#$%&\'()*+,-./:;<=>?,@\\[\\]^_`{|}~].*"));
    }

    // Use HashSet to ensure that all characters are unique
    @Test
    public void test_character_uniqueness() {
        Password pw = new Password();
        pw.GeneratePassword(10);
        String password = pw.GetPassword();

        Set<Character> password_set = new HashSet<>();
        for (char c : password.toCharArray()) {
            password_set.add(c);
        }

        assertTrue(password.length() == password_set.size());
    }

    // Test to ensure no consecutive letters are the same
    @Test
    public void test_no_consecutive_characters() {
        Password pw = new Password();
        pw.GeneratePassword(10);
        String password = pw.GetPassword();

        for (int i = 0; i < password.length() - 1; i++) {
            assertNotEquals(password.charAt(i), password.charAt(i + 1));
        }
    }

    @Test
    public void test_no_consecutive_password_duplication() {
        Password pw = new Password();
        pw.GeneratePassword(10);

        Password pw2 = new Password();
        pw.GeneratePassword(10);

        assertNotEquals(pw.GetPassword(), pw2.GetPassword());
    }
}
