// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BookManagementSys {

    struct Book {
        uint id;
        string bookName;
        string author;
        uint price;
        bool available;
    }

    Book[] public books;
    address owner = msg.sender;

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function addNewBook(uint id, string memory name,
        string memory author, uint price) public onlyOwner {
        books.push(Book(id, name, author, price, true));
    }

    function viewBook(uint index) public view returns (
        uint, string memory, string memory, uint, bool
    ) {
        Book memory b = books[index];
        return (b.id, b.bookName, b.author, b.price, b.available);
    }

    function viewPrice(uint index) public view returns (uint) {
        return books[index].price;
    }

    function updatePrice(uint index, uint price)
        public onlyOwner {
        books[index].price = price;
    }

    function updateAvailability(uint index, bool status)
        public onlyOwner {
        books[index].available = status;
    }

    receive() external payable {}
    fallback() external payable {}
}
