# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_preprocess.ipynb (unless otherwise specified).

__all__ = ['VoxelData']

# Cell
import os
import wandb
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Pydicom related imports
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import SimpleITK as sitk

# Cell
class VoxelData():
    """
    MRI plane type (Axial, Coronal, and Sagittal) is not consistent among patients or MRI scans.
    This class obtain normalized voxels by appropriately rotating MRI voxels.
    """
    def __init__(self, reference_dir:str):
        # Set up SITK reader
        self.reader = sitk.ImageSeriesReader()
        self.reader.LoadPrivateTagsOn()

        # get reference image
        self.reference_image = self.get_reference_image(reference_dir)


    def read_dicom(self, dicom_dir):
        """
        Reads a dicom file and returns the metadata

        Parameters
        ----------
        dicom_dir : str (path to DICOM scan)
        """
        filenamesDICOM = self.reader.GetGDCMSeriesFileNames(dicom_dir)
        self.reader.SetFileNames(filenamesDICOM)
        file = self.reader.Execute()
        return file

    def resample(self, image, ref_image):
        """
        Resamples the image to the same size and orientation as the reference image

        Parameters
        ----------
        image : SimpleITK image
        ref_image : Reference SimpleITK image
        """
        resampler = sitk.ResampleImageFilter()
        resampler.SetReferenceImage(ref_image)
        resampler.SetInterpolator(sitk.sitkLinear)

        resampler.SetTransform(sitk.AffineTransform(image.GetDimension()))

        resampler.SetOutputSpacing(ref_image.GetSpacing())

        resampler.SetSize(ref_image.GetSize())

        resampler.SetOutputDirection(ref_image.GetDirection())

        resampler.SetOutputOrigin(ref_image.GetOrigin())

        resampler.SetDefaultPixelValue(image.GetPixelIDValue())

        resamped_image = resampler.Execute(image)

        return resamped_image

    def normalize(self, data):
        """
        Normalizes the data to the range [0, 1]

        Parameters
        ----------
        data : numpy array
        """
        return (data - np.min(data)) / (np.max(data) - np.min(data))

    def get_reference_image(self, reference_dir):
        """
        Returns the reference SimpleITK image.

        Parameters
        ----------
        reference_dir : str (path to reference DICOM scan)
        """
        return self.read_dicom(reference_dir)

    def get_voxel_data(self, dicom_dir):
        """
        Returns the voxel data.

        Parameters
        ----------
        dicom_dir : str (path to DICOM scan)
        """
        # Read DICOM
        dicom_image = self.read_dicom(dicom_dir)

        # Resample to the same size and orientation as the reference image
        resampled_image = self.resample(dicom_image, self.reference_image)

        # Normalize to the range [0, 1]
        normalized_image = self.normalize(sitk.GetArrayFromImage(resampled_image))

        return normalized_image