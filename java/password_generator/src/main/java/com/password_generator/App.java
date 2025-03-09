package com.password_generator;

public class App 
{
    public static void main( String[] args )
    {
        Password pw = new Password();
        pw.GeneratePassword(94);
        System.out.println("Your password is:" + pw.GetPassword());
    }
}
