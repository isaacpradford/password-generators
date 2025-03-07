// Requirements: 
// # Generates n length of password
// # No duplicate characters
// # No two same characters next to each other
// # Include special characters, capital letters, lowercase letters, and a number
// # Min length of 8

using System;

namespace Password;

public class PasswordGenerator
{
    private readonly List<char> upper = [.. "ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray()]; // Put relevant characters into arrays
    private readonly List<char> lower = [.. "abcdefghijklmnopqrstuvwxyz".ToCharArray()];
    private readonly List<char> nums = [.. "0123456789".ToCharArray()];
    private readonly List<char> punc = [.. "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~".ToCharArray()];
    private readonly Random random = new();

    public string password = "";

    public void GeneratePassword(int length)
    {
        // Return if it's too short or long
        if (length < 8)
        {
            return;
        }

        if (length > upper.Count + lower.Count + nums.Count + punc.Count)
        {
            return;
        }

        List<List<char>> charSets = [upper, lower, nums, punc]; // Put the available character arrays into a single array

        // Main loop takes the 4 character arrays, picks a random char from a random array in it, removes that char and array
        // On next loop, the only available arrays are ones that it hasn't used yet, ensuring all character types are used
        while (password.Length < length)
        {
            // When there's nothing in the charSets array, add each character array back into the charSets array unless it's already empty
            if (charSets.Count == 0)
            {
                if (upper.Count > 0)
                {
                    charSets.Add(upper);
                }
                if (lower.Count > 0)
                {
                    charSets.Add(lower);
                }
                if (nums.Count > 0)
                {
                    charSets.Add(nums);
                }
                if (punc.Count > 0)
                {
                    charSets.Add(punc);
                }
            }


            int randSetIndex = random.Next(charSets.Count); // Get random # from 0 - length of charSets
            List<char> charSet = charSets[randSetIndex]; // Pick random set from the 4 available character sets using randsetindex
            int randCharIndex = random.Next(charSet.Count); // Grab random index from the chosen charset

            password += charSet[randCharIndex]; // Add that character from the selected array to the Password

            charSet.RemoveAt(randCharIndex); // Remove that character to ensure no duplicates can be used
            charSets.RemoveAt(randSetIndex); // Remove the last used set so that it ensures all charTypes get used
        }

        Console.WriteLine(password);
    }
}