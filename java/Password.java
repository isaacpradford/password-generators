import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Password {
    private ArrayList<Character> upper = new ArrayList<>(Arrays.asList(
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z'));
    private ArrayList<Character> lower = new ArrayList<>(Arrays.asList(
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'));
    private ArrayList<Character> nums = new ArrayList<>(Arrays.asList(
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'));
    private ArrayList<Character> punc = new ArrayList<>(Arrays.asList(
            '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
            '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'));

    private String password = "";

    public void GeneratePassword(int length) {
        if (length < 8) {
            return;
        } else if (length > upper.size() + lower.size() + nums.size() + punc.size()) {
            return;
        }

        List<List<Character>> charSets = new ArrayList<>(Arrays.asList(upper, lower, nums, punc));
        StringBuilder pw = new StringBuilder();
        Random rand = new Random();

        // While loop till the length of the password == the requested length
        while (length > pw.length()) {
            if (charSets.size() == 0) {
                // Re-add char all arrays to CharSets once the charSets is empty
                if (upper.size() > 0)
                    charSets.add(upper);
                if (lower.size() > 0)
                    charSets.add(lower);
                if (nums.size() > 0)
                    charSets.add(nums);
                if (punc.size() > 0)
                    charSets.add(punc);

            }

            System.out.println(charSets);

            int randSetIndex = rand.nextInt(charSets.size()); // Get random index of items in charSets
            List<Character> charSet = charSets.get(randSetIndex); // Set random index of charSets to variable
            int randCharIndex = rand.nextInt(charSet.size()); // Get random char from selected set

            pw.append(charSet.get(randCharIndex)); // Add selected char from selected set

            charSet.remove(randCharIndex); // Remove that character from the selected array
            charSets.remove(randSetIndex); // Remove that set from the array of char sets so that the next random option
                                           // has to be one of the unselected character types
        }

        SetPassword(pw.toString());// put the pw to a string once the loop is ended
    }

    // Getters + Setters
    public void SetPassword(String pw) {
        password = pw;
    }

    public String GetPassword() {
        return password;
    }

    public static void main(String[] args) {
        Password pw = new Password();
        pw.GeneratePassword(94);
        System.out.println("Your password is:" + pw.GetPassword());
    }
}
