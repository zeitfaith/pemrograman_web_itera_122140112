from abc import ABC, abstractmethod

# Abstract class untuk semua item perpustakaan
class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self._item_id = item_id
        self._title = title

    @abstractmethod
    def display_info(self):
        pass

    @property
    def title(self):
        return self._title

    @property
    def item_id(self):
        return self._item_id

# Subclass: Book
class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self._author = author

    def display_info(self):
        print(f"[Book] ID: {self._item_id} | Title: {self._title} | Author: {self._author}")

# Subclass: Magazine
class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number):
        super().__init__(item_id, title)
        self._issue_number = issue_number

    def display_info(self):
        print(f"[Magazine] ID: {self._item_id} | Title: {self._title} | Issue: {self._issue_number}")

# Kelas Library untuk mengelola koleksi
class Library:
    def __init__(self):
        self.__items = []  # Private attribute

    def add_item(self, item: LibraryItem):
        self.__items.append(item)

    def show_all_items(self):
        if not self.__items:
            print("Tidak ada item di perpustakaan.")
        for item in self.__items:
            item.display_info()  # Polymorphism

    def find_by_title(self, title):
        results = [item for item in self.__items if title.lower() in item.title.lower()]
        return results

    def find_by_id(self, item_id):
        for item in self.__items:
            if item.item_id == item_id:
                return item
        return None

# Program interaktif
def main():
    library = Library()

    while True:
        print("\n--- Menu Perpustakaan ---")
        print("1. Tambah Buku")
        print("2. Tambah Majalah")
        print("3. Tampilkan Semua Item")
        print("4. Cari Item berdasarkan Judul")
        print("5. Cari Item berdasarkan ID")
        print("6. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            id = input("Masukkan ID Buku: ")
            title = input("Masukkan Judul Buku: ")
            author = input("Masukkan Nama Penulis: ")
            library.add_item(Book(id, title, author))
            print("Buku berhasil ditambahkan.")
        elif choice == "2":
            id = input("Masukkan ID Majalah: ")
            title = input("Masukkan Judul Majalah: ")
            issue = input("Masukkan Nomor Edisi: ")
            library.add_item(Magazine(id, title, issue))
            print("Majalah berhasil ditambahkan.")
        elif choice == "3":
            library.show_all_items()
        elif choice == "4":
            keyword = input("Masukkan kata kunci judul: ")
            results = library.find_by_title(keyword)
            if results:
                for item in results:
                    item.display_info()
            else:
                print("Item tidak ditemukan.")
        elif choice == "5":
            id = input("Masukkan ID item: ")
            item = library.find_by_id(id)
            if item:
                item.display_info()
            else:
                print("Item tidak ditemukan.")
        elif choice == "6":
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
