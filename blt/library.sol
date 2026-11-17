// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract LibraryManagementSys {

    struct Book {
        uint id;
        string bookName;
        string author;
        uint quantity;
    }

    Book[] public bookRecords;
    address owner = msg.sender;

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function addNewBook(uint id, string memory name,
        string memory author, uint quantity) public onlyOwner {
        bookRecords.push(Book(id, name, author, quantity));
    }

    function viewBook(uint index) public view returns (
        uint, string memory, string memory, uint
    ) {
        Book memory b = bookRecords[index];
        return (b.id, b.bookName, b.author, b.quantity);
    }

    function totalBooks() public view returns (uint) {
        return bookRecords.length;
    }

    function updateQuantity(uint index, uint quantity)
        public onlyOwner {
        bookRecords[index].quantity = quantity;
    }

    receive() external payable {}
    fallback() external payable {}
}
