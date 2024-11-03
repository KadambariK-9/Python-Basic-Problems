#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Account {
    int accountNumber;
    char name[50];
    char password[20];
    float balance;
};

struct Account account;

void createAccount() {
    float initialDeposit;

    account.accountNumber = 1;  
    printf("Enter account holder's name: ");
    scanf("%s", account.name);

    printf("Set a password for your account: ");
    scanf("%s", account.password);

    do {
        printf("Enter initial deposit (minimum 500): ");
        scanf("%f", &initialDeposit);

        if (initialDeposit < 500) {
            printf("Error: Initial deposit must be at least 500. Try again.\n");
        }
    } while (initialDeposit < 500); 

    account.balance = initialDeposit;
    printf("Account created successfully! Your account number is %d\n", account.accountNumber);
}

int verifyAccount() {
    char enteredName[50];
    char enteredPassword[20];

    printf("Enter account holder's name: ");
    scanf("%s", enteredName);

    printf("Enter your password: ");
    scanf("%s", enteredPassword);
    if (strcmp(account.name, enteredName) == 0 && strcmp(account.password, enteredPassword) == 0) {
        return 1;  
    } else {
        printf("Error: Incorrect name or password.\n");
        return 0;  
    }
}

void viewAccount() {
    if (verifyAccount()) {
        printf("Account Number: %d\n", account.accountNumber);
        printf("Account Holder: %s\n", account.name);
        printf("Balance: %.2f\n", account.balance);
    }
}

void depositMoney() {
    if (verifyAccount()) {
        float amount;
        printf("Enter amount to deposit: ");
        scanf("%f", &amount);
        account.balance += amount;
        printf("Amount deposited successfully! Your new balance is: %.2f\n", account.balance);
    }
}

void withdrawMoney() {
    if (verifyAccount()) {
        float amount;
        printf("Enter amount to withdraw: ");
        scanf("%f", &amount);

        if (account.balance <= 500) {
            printf("Withdrawal not allowed. Balance is 500 or less. Minimum balance of 500 must be maintained.\n");
        } else if (account.balance - amount < 500) {
            printf("Insufficient balance. After withdrawal, minimum balance of 500 must be maintained.\n");
        } else {
            account.balance -= amount;
            printf("Amount withdrawn successfully! Your new balance is: %.2f\n", account.balance);
        }
    }
}

int main() {
    int choice;
    account.accountNumber = 0;  // Initialize with no account

    while (1) {
        printf("\nBanking Management System\n");
        printf("1. Create Account\n");
        printf("2. View Account\n");
        printf("3. Deposit Money\n");
        printf("4. Withdraw Money\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                createAccount();
                break;
            case 2:
                if (account.accountNumber == 0) {
                    printf("No account found. Create an account first.\n");
                } else {
                    viewAccount();
                }
                break;
            case 3:
                if (account.accountNumber == 0) {
                    printf("No account found. Create an account first.\n");
                } else {
                    depositMoney();
                }
                break;
            case 4:
                if (account.accountNumber == 0) {
                    printf("No account found. Create an account first.\n");
                } else {
                    withdrawMoney();
                }
                break;
            case 5:
                printf("Exiting...\n");
                exit(0);
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
