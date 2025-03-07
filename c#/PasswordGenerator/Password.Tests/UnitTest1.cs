using Xunit;
using System;
// using System.Linq;

using Password;

namespace Password.Tests;


public class UnitTest1
{
    [Fact]
    public void Test_Length()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(12);

        Assert.Equal(12, pw.password.Length);
    }

    [Fact]
    public void Test_Min_Length()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(6);

        Assert.Equal(0, pw.password.Length);
    }

    [Fact]
    public void Test_Max_length()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(95);

        Assert.Equal(0, pw.password.Length);
    }

    [Fact]
    public void Test_Operational_Max_length()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(94);

        Assert.Equal(94, pw.password.Length);
    }

    [Fact]
    public void Test_Has_Capital()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(10);

        Assert.Contains(pw.password, char.IsUpper);
    }

    [Fact]
    public void Test_Has_Lower_Case()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(10);

        Assert.Contains(pw.password, char.IsLower);
    }
    [Fact]
    public void Test_Has_Special_Char()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(10);

        Assert.Contains(pw.password, char.IsPunctuation);
    }
    [Fact]
    public void Test_Has_Number()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(10);

        Assert.Contains(pw.password, char.IsDigit);
    }

    [Fact]
    public void Test_Has_All_Unique_Characters()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(50);

        HashSet<char> password_hash = [.. pw.password];
        Assert.True(pw.password.Length == password_hash.Count);
    }

    [Fact]
    public void Test_No_Consecutive_Characters()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(30);

        for (int i = 0; i < pw.password.Length - 1; i++)
        {
            Assert.True(pw.password[i] != pw.password[1 + i]);
        }
    }

    [Fact]
    public void Test_Consecutive_Password_Duplication()
    {
        PasswordGenerator pw = new();
        pw.GeneratePassword(8);

        PasswordGenerator pw2 = new();
        pw.GeneratePassword(8);

        Assert.NotEqual(pw.password, pw2.password);
    }
}
