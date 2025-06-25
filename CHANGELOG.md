# DeliciousBytes Library Change Log

## [1.0.2] - 2025-06-17
### Added
- Added support for creating `Bytes` values from `bytes` values.
- Added a new `BytesView` class for iterating over `bytes` and `bytearray` objects with
the ability to access the data as arbitrarily sized groups of bytes as well as being able
to cast bytes to specific data types.
- Added `Float`, `Float16`, `Float32` and `Float64` types, as well as `Double` (an alias for `Float64`).
- Added `Size`, `SingedSize` and `UnsignedSize` integer subtypes which have a maximum size dependent upon the system they are running on.
- Added `Unicode`, `UTF8`, `UTF16`, `UTF32`, `ASCII` types to compliment the `String` type; these string variants hold strings with different default character encodings.
- Added `Type` superclass as a parent of all of the type subclasses which makes type comparison and class hierarchy membership easier to discern and allows shared behaviour to be centrally defined and maintained.

### Changed
- The `Short` type was previously unsigned and is now signed as per the C standard following the Python convention; the `Short` type was previously based on embedded metadata standards, which treat `short` as unsigned and defined a separate `signed short`.
- The `Long` type was previously unsigned and is now signed as per the C standard following the Python convention; the `Long` type was previously based on embedded metadata standards, which treat `long` as unsigned and defined a separate `signed long`.
- The `LongLong` type was previously unsigned and is now signed as per the C standard following the Python convention; the `LongLong` type was previously based on embedded metadata standards, which treat `long long` as unsigned and defined a separate `signed long long`.
- A new `UnsignedShort` type has been added to compliment the signed `Short` type and pairs with the `SignedShort` type which is functionally equivalent to `Short`.
- A new `UnsignedLong` type has been added to compliment signed `Long` type and pairs with the `SignedLong` type which is functionally equivalent to `Long`.
- A new `UnsignedLongLong` type has been added to compliment signed `LongLong` type and pairs with the `SignedLongLong` type which is functionally equivalent to `LongLong`.

## [1.0.1] - 2025-06-11
### Added
- Improved input validation for `String.encode()` and `String.decode()`.
- Added support for decoding `String` values from bytes in LSB order.

## [1.0.0] - 2025-06-10
### Added
- First release of the DeliciousBytes library.
