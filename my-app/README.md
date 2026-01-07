# Secure PDF Page-by-Page Viewer (POC)

## Problem
Directly serving PDF files to clients is insecure and inefficient,
especially for large documents.

## Solution
This project implements a secure, on-demand PDF page rendering system.
PDFs are stored privately on the backend. Pages are rendered as images
only when requested and cached to avoid repeated computation.

## Architecture
- Frontend (React): requests individual page images
- Backend (Flask): handles access control, rendering, caching
- Database: stores PDF metadata
- Storage: stores original PDFs
- Cache: stores rendered page images

(Architecture diagram link)

## Key Features
- No direct PDF access from client
- Page-level rendering
- Filesystem caching
- Browser caching (304 Not Modified)

## Tech Stack
- Frontend: React
- Backend: Flask, PyMuPDF
- Database: SQLite
- Cache: Filesystem (POC)

## How to Run
1. Start backend
2. Start frontend
3. Open viewer and navigate pages
