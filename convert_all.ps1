# Convert all products
$products = @(
    @{Dir="5-ALA"; File="5ALA Presentation tiếng Việt.pptx"; Type="pptx"},
    @{Dir="Acropass"; File="Quotation of Acropass Beauty_20205_ ver01.pptx"; Type="pptx"},
    @{Dir="Albumin"; File="Quotation of Albumin Drinking.pptx"; Type="pptx"},
    @{Dir="AmabiRes"; File="AmabiRis Quotation 2025_ver01.pptx"; Type="pptx"},
    @{Dir="Cmarox"; File="Trace Mineral Cmarox Quotation_2025_Ver02.pptx"; Type="pptx"},
    @{Dir="ProImmilk"; File="Quotation of ProImmilk.pptx"; Type="pptx"},
    @{Dir="Quotation of Cancer Products"; File="ODM-0EM 2025.xlsx"; Type="xlsx"}
)

foreach ($product in $products) {
    Write-Host "`n=== Converting $($product.Dir) ===" -ForegroundColor Cyan
    
    # Change to product directory to avoid encoding issues with file names
    Push-Location "Products\$($product.Dir)"
    
    try {
        # Convert to markdown (using relative paths from product directory)
        python3.12 ..\..\convert_pptx_to_markdown.py $($product.File) "README.md"
        
        # Extract images (only for PowerPoint files)
        if ($product.Type -eq "pptx") {
            python3.12 extract_images.py
            python3.12 create_dummy_images.py
        }
        
        Write-Host "✓ Completed $($product.Dir)" -ForegroundColor Green
    }
    catch {
        Write-Host "✗ Error in $($product.Dir): $_" -ForegroundColor Red
    }
    finally {
        Pop-Location
    }
}

Write-Host "`n=== All conversions completed! ===" -ForegroundColor Green